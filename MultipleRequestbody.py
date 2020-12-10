from fastapi import FastAPI, Query, Path, Body
from fastapi.middleware.cors import CORSMiddleware
import nest_asyncio
from pyngrok import ngrok
import uvicorn
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

class User(BaseModel):
    username: str
    full_name: str = None

@app.get('/')
async def root():
    return {'hello': 'world'}

# Expecting three request body item user and q(body keyword says that this parameter should be as a request body and "...." makes it as a required parameter)
@app.put("/items_new/{item_id}")
async def update_item(*, item_id: int, item: Item, user: User, q: int = Body(...)):
    results = {"item_id": item_id, "item": item, "user": user, "q" : q}
    return results

# embed means making item as a key and request body as a value
@app.put("/items_new/{item_id}")
async def update_item(*, item_id: int, item: Item = Body(..., embed = True)):
    results = {"item_id": item_id, "item": item}
    return results

ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)
