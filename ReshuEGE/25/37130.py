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
    for e in ds:
        if e % 10 == 7 and e != 7 and e != n:
            return e
    return 0

n = 600001
a = []
while len(a) < 5:
    res = func(n)
    if 0 < res:
        a.append((n, res))
    n += 1
print(a)