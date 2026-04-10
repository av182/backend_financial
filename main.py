import uvicorn
from fastapi import FastAPI
import requests
import json

app = FastAPI(title='Finance Application', version='1.0.0')


@app.get("/")
async def index():
    return {'msg': "Hello, world!"}
   

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=9011, reload = True) 
