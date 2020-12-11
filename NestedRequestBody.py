import uvicorn
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Set, Dict
from fastapi.middleware.cors import CORSMiddleware
import nest_asyncio
from pyngrok import ngrok

app = FastAPI(debug = True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str = Field(None, title="Description of the item", max_length=250)  # Field Validation 
    price: float = Field(..., gt=0, le=100, description="The price must be greater than zero and lesser than or equal to 100") # Field Validation
    tax: float = None
    # tags: List[str]  # This will convert all value's type as string same for int and float(Type Convertion)
    tags: Set[str] = [] # This will remove the duplicates
    images: List[Image] = None #nesting image model


class Offer(BaseModel):
    name: str
    description: str = None
    price: float
    items: List[Item] # list of items model (nesting)


@app.put("/items/{item_id}")
async def update_item(*, item_id: int, offers: List[Offer]): # list of offers model
    results = {"item_id": item_id, "Offer": offers}
    return results


@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights

ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)
