from fastapi import FastAPI,Header
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

## Hearder Class

@app.get("/items/")
async def read_items(*, ads_id: str = Header("abc")):  ## Default Value
    return {"ads_id": ads_id} 


@app.get("/itemsOne/")
async def read_items(*, user_agent: str = Header(None)):  ## Optional
    return {"User-Agent": user_agent}


@app.get("/itemsTwo/")
async def read_items(*, strange_header: str = Header(None, convert_underscores=False)):  ## By default it converts the underscores to hyphen,But now it will not
    return {"strange_header": strange_header}


ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)
