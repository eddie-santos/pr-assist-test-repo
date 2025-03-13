def fibonacci(n): 
    terms = [0, 1]
    for i in range(n):
        if i <= 1:
            continue
        terms.append(terms[i-1] + terms[i-2])
    return terms[-1]

def power(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result

def factorial(n): 
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_even(n):  
    return n % 2 == 0

def add_nums(x,y):
    sm = x + y
    return sm

def sort_list(lst): 
    return lst

def unused_function():
    pass