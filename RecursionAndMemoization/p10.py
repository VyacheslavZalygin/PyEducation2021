import sys
from tkinter import E
# Построить автомат по S
# функция kmp возвращает номер вершины, куда перейдёт автомат из вершины k через ребро x
ALPHABET = [chr(x) for x in range(ord('a'), ord('b')+1)]
print(ALPHABET)

def func(S):
    if len(S) != 0:
        func(S[:-1])
    print(S)

def build_kmp(S):
    # номер вершины
    n = len(S)    
    # самая первая вершина (ссылается на саму себя)
    if n == 0: 
        def kmp(k, x):
            return 0
        return kmp
    else:
        old_kmp = build_kmp(S[:-1])
        # старый kmp, но с затёртым значением
        def prev_kmp(k, x):
            # точно ли спрашиваем эту вершину, а не предыдущую (прокидываем, если придыдущую)
            if x == S[-1] and k+1 == n:
                # создаём новое ребро, которое будет вести на новую вершину
                return n
            # остальных случаях делаем как обычно
            return old_kmp(k, x)
        
        # k - номер вершины, с которой делаем ход, x - по какому ребру
        def kmp(k, x):
            if k != n:
                # если спрашивают не нашу вершину, то спрашиваем предыдущую
                return prev_kmp(k, x)
            else:
                # вершина, которую мы копируем
                copy = old_kmp(k, x)
                return prev_kmp(copy, x)
        return kmp

# print(func("abc"))
# S, *pairs = sys.stdin.read().split()
# pairs = [(int(pairs[i]), pairs[i+1]) for i in range(0, len(pairs), 2)]
# kmp = build_kmp(S)
# print(*[kmp(k, x) for k, x in pairs])
kmp = build_kmp('aba')
print(kmp(2, 'a')) # 3
print(kmp(2, 'b')) # 0
print(kmp(1, 'b')) # 2
print(kmp(1, 'a')) # 1
print(kmp(3, 'b')) # 2
print(kmp(3, 'a')) # 1