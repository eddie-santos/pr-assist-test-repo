import random

def fibonacci(n):
    """The Fibonacci Sequence!"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    a, b = 0, 1
    sequence = [a, b]
    for _ in range(2, n):
        next_num = a + b
        a, b = b, next_num
        sequence.append(next_num)
    return sequence

def power(x: float, n: int):
    """Calculate x to the power of n"""
    ans = 1
    for _ in range(n):
        ans *= x
    return ans

def factorial(n):
    """Calculates the factorial of a number n
    
    Arguments:
      n: number to generate factorial for

    Returns:
      The factorial value corresponding to the number n
    """ 
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_even(n):  
    return n % 2 == 0

def add_nums(x,y):
    sm = x + y
    return sm

def sort_list(l): 
    """
    Sorts a list of numbers using the incredibly inefficient Bogosort algorithm.

    Args:
        arr: The list of numbers to be sorted.

    Returns:
        The sorted list (eventually).
    """

    def is_sorted(l):
        """
        Checks if a list is sorted in ascending order.
        """
        return all(l[i] <= l[i + 1] for i in range(len(l) - 1))

    while not is_sorted(l):
        random.shuffle(l)  # Randomly shuffle the list
    return l

def unused_function():
    pass