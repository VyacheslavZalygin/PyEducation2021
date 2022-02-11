import sys

# Вычислять числа grundy от 0 до n, строя граф, пока не замечаем значение, которое уже знаем

# def grundy(v):
#     b = set()
#     for i, n in enumerate(v): # для каждого кусочка
#         for j in range(0, (n-2)//2+1): # все варианты перестановок
#             b.add(grundy((*v[:i], *((j, n-j-2) if j != 0 else (n-j-2,)), *v[i+1:])))
#     res = 0
#     while res in b: res += 1
#     return res

# cached = grundy
# cache = {}
# def grundy(v):
#     if v not in cache:
#         cache[v] = cached(v)
#     return cache[v]

def grundy(n):
    if n < 1: return 0
    targets = set()
    for x in range((n-2)//2+1):
        targets.add(grundy(x) ^ grundy(n-x-2))
    res = 0
    while res in targets: res += 1
    return res

cached = grundy
cache = {}
def grundy(n):
    if n not in cache:
        cache[n] = cached(n)
    return cache[n]

N = int(sys.stdin.read())
print(2 if grundy(N) == 0 else 1)