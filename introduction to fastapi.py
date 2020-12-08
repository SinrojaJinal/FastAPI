from fastapi import FastAPI
import uvicorn

app = FastAPI(debug=True)

@app.get('/')
async def root():
  return {message: "Hello World"}
