import sys
# Построить автомат по S
# функция kmp возвращает номер вершины, куда перейдёт автомат из вершины k через ребро x
ALPHABET = [chr(x) for x in range(ord('a'), ord('z')+1)]
print(ALPHABET)

def func(S):
    if len(S) != 0:
        func(S[:-1])
    print(S)

def build_kmp(S):
    if len(S) == 0: 
        def kmp(k, x):
            return 0
        return kmp
    old_kmp = build_kmp(S[:-1])
    old_kmp(1, S[-1])
    def old_kmp(k, x):
        pass
    def kmp(k, x):
        pass
    return kmp


# print(func("abc"))
# S, *pairs = sys.stdin.read().split()
# pairs = [(int(pairs[i]), pairs[i+1]) for i in range(0, len(pairs), 2)]
# kmp = build_kmp(S)
# print(*[kmp(k, x) for k, x in pairs])