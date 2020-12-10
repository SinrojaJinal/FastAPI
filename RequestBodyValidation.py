import uvicorn
from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field
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

class Item(BaseModel):
    name: str
    description: str = Field(None, title="Description of the item", max_length=250)
    price: float = Field(..., gt=0, le=100, description="The price must be greater than zero and lesser than or equal to 100")
    tax: float = None


class User(BaseModel):
    username: str
    full_name: str = None

@app.get(/)
async def root():
    return {"message" : "Hello World"}

@app.put("/items/{item_id}")
async def update_item(*, item_id: int, item: Item = Body(..., embed=True, example={
            "name": "Foo",
            "description": "A very nice Item",
            "price": 35.4,
            "tax": 3.2,
        },)):
    results = {"item_id": item_id, "item": item}
    return results

ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)
