from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/callname/{name}")
def get_call_name(name: str = None):
    return {"hello": name}

@app.post("/callname")
def post_call_name(name: str = "Paipibut"):
    return {"hello": name}

handler = Mangum(app)
