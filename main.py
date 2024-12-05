from fastapi import FastAPI, HTTPException
from utils import algos

app = FastAPI()


@app.get("/fibonacci/{n}")
async def get_fibonacci(n: int):
    if n <= 0:
        raise HTTPException(status_code=400, detail="Input must be positive")
    return {"result": algos.fibonacci(n)}


@app.get("/power/{x}/{n}")
async def get_fibonacci(x: float, n: int):
    return {"result": algos.power(x, n)}


@app.get("/factorial/{n}")
async def get_factorial(n: int):
    return {"result": algos.factorial(n)}


@app.get("/divide/{a}/{b}")
async def divide(a: float, b: float):
    return {"result": a / b}


@app.post("/reverse-string")
async def reverse_string(input_string: str):
    return {"reversed": input_string[::-1]}


@app.get("/square/{n}")
async def square(n: float):
    return {"result": n * n}


@app.get("/sqrt/{n}")
async def sqrt(n: float):
    if n < 0:
        raise HTTPException(status_code=400, detail="Input must be non-negative")
    return {"result": n**0.5}


@app.get("/log/{n}")
async def log(n: float):
    if n <= 0:
        raise HTTPException(status_code=400, detail="Input must be positive")
    return {"result": algos.logarithm(n)}

