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

def sum(n):
    ds = divisors(n)
    if len(ds) < 3:
        return 0
    return ds[1] + ds[-2]

n = 700001
a = []
while len(a) < 5:
    res = sum(n)
    if 0 < res and res % 10 == 8:
        a.append((n, res))
    n += 1

print(a)