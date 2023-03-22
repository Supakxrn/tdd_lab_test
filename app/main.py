from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/callname/{name}")
def call_name(name: str = None):
    return {"hello": name}

@app.post("/callname")
def call_name(name: str = None):
    return {"hello": name}

handler = Mangum(app)