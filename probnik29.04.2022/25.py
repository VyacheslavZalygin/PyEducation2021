def div(n):
    res = set()
    i = 1
    while i*i <= n:
        if n % i == 0:
            res.add(i)
            res.add(n//i)
        i += 1
    return sorted(res)

def v(n):
    return [x for x in div(n) if x % 2 == 1]

for n in range(95632, 95650+1):
    res = v(n)
    if len(v(n)) == 6:
        print(n, res)