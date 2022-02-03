def f(n):
    n = bin(n)[2:]
    n += n[-2]
    n += n[1]
    return int(n, 2)

for n in range(20, 100):
    if f(n) > 180:
        print(n)
        break