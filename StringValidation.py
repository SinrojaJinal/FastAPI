from fastapi import FastAPI ,Query
from fastapi.middleware.cors import CORSMiddleware
import nest_asyncio
from pyngrok import ngrok
import uvicorn
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/')
async def root():
    return {'hello': 'world'}

# max min length and regular expression validation ,default value (put value instead of ... this)and optional parameter(put None instead of ... this)
@app.get("/items/")
async def get_items(item_id: str = Query(..., min_length = 2, max_length = 10, regex="^Item\d{1,6}")):#... means required value
    return {"item": item_id}

# passing a list as a default value,metadata about the properties(deprecation ,title and description) and alias name
@app.get("/items/")
async def get_items(item_id: List[str] = Query(["Pen", "Pencil"], # list as a parameter
                                               title = "Item List", # metadata
                                               description = "List of items to be returned.",# metadata
                                               min_length = 2, max_length = 10, deprecated = True, # depricarting parameters
                                               alias = "item-id")): # Alias name
    results = {"items": item_id}
    return results
ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)
