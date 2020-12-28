from fastapi import FastAPI, UploadFile, File
from fastapi.encoders import jsonable_encoder
import uvicorn
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello"}

@app.post("/create_file/")
async def create_file(myfile: UploadFile = File(...)):
    print(myfile.file)
    # print('../'+os.path.isdir(os.getcwd()+"images"),"*************")
    try:
        os.mkdir("files")
        print(os.getcwd()) # os.getcwd() method tells us the location of current working directory (CWD).
    except Exception as e:
        print(e) 
    file_name = os.getcwd()+"/files/"+myfile.filename.replace(" ", "-")
    with open(file_name,'wb+') as f:
        f.write(myfile.file.read())
        f.close()
    return {"filename": file_name}
