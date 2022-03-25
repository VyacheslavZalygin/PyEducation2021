def f(n):
    n = bin(n)[2:]
    n += n[-1]
    n += str(sum([int(x) for x in n]) % 2)
    return int(n, 2)


great = set()
for n in range(1000):
    r = f(n)
    if r > 105:
        great.add(r)
print(min(great))
