def f(n):
    n = bin(n)[2:]
    for _ in range(2):
        s = sum([int(x) for x in n])
        n += str(s % 2)
    return int(n, 2)

for n in range(10, 100):
    if f(n) > 154:
        print(n)
        break