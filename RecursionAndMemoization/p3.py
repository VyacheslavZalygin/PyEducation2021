import sys

# sys.setrecursionlimit(10000)
# n - яйца, k - этажи
n_max, k_max = [int(x) for x in sys.stdin.read().split()]

def eggs(n, k):
    if n == 0: return 1
    if k < 1: return 1
    a = eggs(n-1, k)
    b = eggs(n, k_max-k-1)
    return 1+max(a, b)

print(min([eggs(n_max, x) for x in range(1, k_max+1)]))

# бросить с любого этажа, посчитать, сколько нужно, если оно разбилось, сколько нужно, чтобы оно не разбилось - выбрать максимальное
# тоже самое для любого другого этажа, найти минимальное (самой оптимальный алгоритм)
# если яйцо не разбилось - можно использовать ещё раз
# минимум среди максимов

# f(я, э) => max(1 + min_x (0 <= x <= э+1) (f(я-1, x), f(я, э-1-x) ))