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
    if len(ds) >= 4:
        return ds[-2] + ds[-3]
    return 0

a = []
n = 11000001
while len(a) < 5:
    s = sum(n)
    if 0 < s < 10000:
        a.append((n, s))
    n += 1
print(a)