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

def isPrime(n):
    return len(divisors(n)) == 2

for i in range(101000000, 102000001, 2):
    if i == int(i):
        if isPrime((i//2)**0.5):
            print(i)