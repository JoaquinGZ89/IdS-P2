from fastapi import FastAPI # type: ignore

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

from code_1 import sum

@app.get("/sum")
def get_sum(a: int, b: int):
    return {"sum": sum(a, b)}


