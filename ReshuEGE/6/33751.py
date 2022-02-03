def f(s):
    s = (s + 1) // 7
    n = 36
    while s < 2050:
        s = s * 2
        n = n + 3
    return n

for s in range(6, 1000):
    if f(s) == 66:
        print(s)
        break