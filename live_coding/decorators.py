import time
import random
from functools import wraps


# Write a decorator that prints the execution time of a function.
def track_time(func):
    def wrapper():
        start = time.time()
        func()
        print(time.time() - start)
    return wrapper

@track_time
def long_func():
    time.sleep(random.uniform(0,2))

# long_func()

# Create a decorator that logs function arguments before calling the function.
def log_arguments(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

@log_arguments
def square(x: int):
    return x ** 2

# print(square(10))

# Implement a decorator that caches results of a function (simple memoization).
cache = {}

def cache_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (func, args, frozenset(kwargs.items()))
        if key in cache:
            print("Cache has been hit!")
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper

@cache_result
def square(x: int):
    return x ** 2

print(square(10))
print(square(10))
print(square(9))
print(square(9))
