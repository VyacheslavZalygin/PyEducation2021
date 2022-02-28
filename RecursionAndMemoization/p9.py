import sys
# Построить автомат по S
# функция kmp возвращает номер вершины, куда перейдёт автомат из вершины k через ребро x
ALPHABET = [chr(x) for x in range(ord('a'), ord('z')+1)]

def process_kmp(S):
    n = len(S)
    if n == 0:
        table = {}
        for l in ALPHABET: table[(n, l)] = 0
        return n, table
    x = S[-1]
    prev, table = process_kmp(S[:-1])
    copy = table[(prev, x)]
    table[(prev, x)] = n
    for l in ALPHABET:
        table[(n, l)] = table[(copy, l)]
    return n, table

def build_kmp(S):
    table = process_kmp(S)[1]
    return lambda k, x: table[(k, x)]

S, *pairs = sys.stdin.read().split()
pairs = [(int(pairs[i]), pairs[i+1]) for i in range(0, len(pairs), 2)]
kmp = build_kmp(S)
print(*[kmp(k, x) for k, x in pairs])