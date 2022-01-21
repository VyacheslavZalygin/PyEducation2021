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

def mul(n):
    ds = divisors(n)
    if len(ds) < 7:
        return 0
    res = 1
    for e in ds[1:6]:
        res *= e
    return res

n = 500000001
a = []
while len(a) < 5:
    res = mul(n)
    if 0 < res < n:
        a.append((n, res))
    n += 1
print(a)