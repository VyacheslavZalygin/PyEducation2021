from functools import lru_cache

# +2, +4, *2
@lru_cache(None)
def f(a, b, t=0): 
    if a == b and t == 8:  return 1
    if a > b:   return 0
    else:       return f(a+2, b, t+1) + f(a+4, b, t+1) + f(a*2, b, t+1)

print(f(4, 64))