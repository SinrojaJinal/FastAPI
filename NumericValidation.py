from fastapi import FastAPI, Query, Path
from fastapi.middleware.cors import CORSMiddleware
import nest_asyncio
from pyngrok import ngrok
import uvicorn

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

## Numeric Validation

# Path Parameter Validation(We can't make path parameter as optional parameter ,it is always required)
@app.get("/items/{item_id}")
async def get_items(item_id: str = Path(..., min_length = 2, max_length = 10, regex="^Item\d{1,6}")):
    return {"item_id": item_id}

# path parameter and query parameter

@app.get("/items/{item_id}")
async def get_items(item: str = Query(None), item_id: str = Path(..., min_length = 2, max_length = 10, regex="^Item\d{1,6}")):
    return {"item_id": item_id, "item" : item}

# gt = greater than ge = greater than or equal to, similarly for the lt and le
@app.get("/items/{item_id}")
async def get_items(item_id: float = Path(..., le = 10, ge = 2, alias = "Item-id", title = "Item Id")):
    return {"item_id": item_id}

ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)
