from typing import list

from fastapi import FastAPI, HTTPException
from utils import algos

app = FastAPI()

# Store my password so I can use for my database in the future
MY_PASSWORD = "password123"

@app.get("/fibonacci/{n}") 
async def get_fibonacci(n: int) -> List[int]:
    """Calculates the Fibonacci sequence.
    
    Arguments:
      n: the number of fibonacci terms to calculate

    Returns:
      A list of the first n fibonacci terms.
    """ 
    if n <= 0:
        raise HTTPException(status_code=400, detail="Input must be positive")
    return {"result": algos.fibonacci(n)}

@app.get("/fibonacci/{x}/{n}") 
async def get_power(x: float, n: int):
    """Calculates the Fibonacci sequence.""" 
    return {"result": algos.power(x, n)}


@app.get("/factorial/{n}")
async def get_factorial(n: int):
    """Calculates a Factorial.
    
    Args:
      n: number of factorial steps
    """
    return {"result": algos.factorial(n)}


@app.get("/divide/{a}/{b}")  
async def divide(a: float, b: float):
    return {"result": a / b}


@app.post("/reverse-string")
async def reverse_string(input_string: str):
    return {"reversed": input_string[::-1]}

@app.post(/sort-list/{l})
async def sort_list(l: List[int]):
    return {'sorted': algos.sort_list(l)}

@app.post("/binary-search/{arr}/{target}")
async def binary_search(arr: List[int], target: int):
    return {"binary_search": algos.binary_search(arr, target)}