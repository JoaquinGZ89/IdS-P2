from fastapi import FastAPI, Query # type: ignore

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

from code_1 import sum

@app.get("/sum")
def get_sum(a: int = Query(...), b: int = Query(...)):
    return {"sum": sum(a, b)}

#Ejemplo de url: '.../sum?a=4&b=6'
