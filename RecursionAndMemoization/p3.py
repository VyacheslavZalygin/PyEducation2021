import sys

sys.setrecursionlimit(20000)
# n - яйца, k - этажи
def eggs(n, k):
    if k == 1: return 1
    return 1+min([max(eggs(n-1, x), eggs(n, k-x-1)) for x in range(0, k)])

table = {}
temp = eggs
def eggs(n, k):
    if (n, k) not in table:
        table[(n, k)] = temp(n, k)
    return table[(n, k)]

print(eggs(*[int(x) for x in sys.stdin.read().split()]))

# бросить с любого этажа, посчитать, сколько нужно, если оно разбилось, сколько нужно, чтобы оно не разбилось - выбрать максимальное
# тоже самое для любого другого этажа, найти минимальное (самой оптимальный алгоритм)
# если яйцо не разбилось - можно использовать ещё раз
# минимум среди максимов

# f(я, э) => min(1 + max_x (0 <= x <= э+1) (f(я-1, x), f(я, э-1-x) ))