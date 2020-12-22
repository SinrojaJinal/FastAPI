from fastapi import FastAPI, File
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import nest_asyncio
from pyngrok import ngrok

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}

ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)
