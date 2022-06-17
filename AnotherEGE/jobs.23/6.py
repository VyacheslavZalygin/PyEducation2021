import sys
from functools import lru_cache

@lru_cache(None)
def f(a, b):
    if a == b:  return 0
    if a > b:   return None
    r = [f(a+1, b), f(a*2, b), f(a*3, b)]
    r = [x if x != None else 100000 for x in r]
    return min(r)+1

# sys.setrecursionlimit(10000)
a = f(1, 9217)
print(a)