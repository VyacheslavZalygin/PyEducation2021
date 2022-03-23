def f(n):
    n = bin(n)[2:]
    if int(n) % 2 == 0:
        n = n[:-1] + '01'
    else:
        n = n[:-1] + '10'
    return int(n, 2)


for n in range(10000):
    if f(n) == 2017:
        print(n)
        break

print(f(1008))
