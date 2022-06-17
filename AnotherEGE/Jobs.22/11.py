def f(a):
    r = 17
    l = 0
    while a >= r:
        l += 1
        a -= r
    if a < l:
        l, a = a, l
    return l, a

for n in range(1000000, 100000, -1):
    if n % 100 == 0:
        print(n)
    if f(n) == (13, 29411):
        print(n)
        break