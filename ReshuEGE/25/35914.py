def divisors(n):
    d = 1
    ds = []
    while d*d <= n:
        if n % d == 0:
            ds.append(d)
            if d*d != n:
                ds.append(n//d)
        d += 1
    ds.sort()
    return ds

def func(n):
    ds = divisors(n)
    count = 0
    for e in ds:
        if e % 2 == 1:
            count += 1
    return count == 5

a = []
for n in range(45000000, 50000001):
    print(n)
    if func(n):
        a.append(n)
        print(True)
# работает слишком долго