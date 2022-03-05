from functools import cmp_to_key
import sys

GREAT = 1
LESS = -1
EQUAL = 0

def dumb_cmp(a, b):
    if   a > b: return GREAT
    elif a < b: return LESS
    else:       return EQUAL

def cmp(k, a, b):
    if k == 1: return dumb_cmp(T[a:a+1], T[b:b+1])
    res = cmp(k//2, a, b)
    return res if res == GREAT or res == LESS else cmp(k, a+k//2, b+k//2) 

cache = {}
tmp = cmp
def cmp(k, a, b):
    if (k, a, b) not in cache:
        cache[(k, a, b)] = tmp(k, a, b)
    return cache[(k, a, b)]

T = sys.stdin.read().strip()
N = 1
while N < len(T): N *= 2
index = sorted(
    range(len(T)+1), 
    key=cmp_to_key(lambda a, b: cmp(N, a, b))
    )

print(*index)