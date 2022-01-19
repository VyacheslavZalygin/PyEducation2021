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
    if len(ds) < 4:
        return 0
    return ds[1] + ds[-2]

n = 452022
a = []
while len(a) < 5:
    res = sum(n)
    if res % 7 == 3:
        a.append((n, res))
    n += 1
print(a)