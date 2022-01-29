def f(n):
    n = bin(n)[2:]
    n = n[:-1]
    n += n[1] + n[1]
    return int(n, 2)

for n in range(100, 1, -1):
    if f(n) <= 76:
        break
    print(n)

print(40, f(40))