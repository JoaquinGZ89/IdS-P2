from fastapi import FastAPI

app = FastAPI()

# Definición de la función suma
def sum(a, b):
    return a + b

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Parte opcional para ejecutar la función suma cuando se ejecute el script directamente
if __name__ == "__main__":
    suma = sum(4, 6)
    print(f'El resultado es: {suma}')

