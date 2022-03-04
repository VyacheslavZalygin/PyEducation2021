from functools import cmp_to_key
import sys

GREAT = 1
LESS = -1
EQUAL = 0

def dumb_cmp(a, b):
    if   a > b: return GREAT
    elif a < b: return LESS
    else:       return EQUAL

def cmp(k, a, b, l):
    if k == 1: return dumb_cmp(T[a:a+l], T[b:b+l])
    res = cmp(k//2, a, b, l)
    return res if res == GREAT or res == LESS else cmp(k, a, b, l+k) 

cache = {}
tmp = cmp
def cmp(k, a, b, l):
    if (k, a, b, l) not in cache:
        cache[(k, a, b, l)] = tmp(k, a, b, l)
    return cache[(k, a, b, l)]

T = sys.stdin.read().strip()
N = 1
while N < len(T): N *= 2
index = sorted(
    range(len(T)+1), 
    key=cmp_to_key(lambda a, b: cmp(N, a, b, 1))
    )

print(*index)