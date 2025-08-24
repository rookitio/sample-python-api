from fastapi import FastAPI
from typing import Dict

app = FastAPI()

@app.get("/hello")
async def hello():
    return {"hello": "world"}

@app.post("/hello")
async def hello_post(payload: Dict):
    return payload