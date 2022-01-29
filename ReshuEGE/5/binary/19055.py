def f(n):
    n = bin(n)[2:]
    for _ in range(2):
        n += str(sum([int(x) for x in n]) % 2)
    return int(n, 2)

for n in range(1, 100):
    if f(n) > 97:
        print(f(n))
        break