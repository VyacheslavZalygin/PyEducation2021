from functools import lru_cache

@lru_cache(None)
def f(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a+1, b) + f(a+2, b) + f(a+4, b)