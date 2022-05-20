# >= 6 нетривиальных нечётных делителей
# m  a * b * c * something
# a, b, c, abc, a*something, b*something, c*something, something

def d(n):
    i = 2
    res = []
    while i*i <= n:
        if n % i == 0:
            if i % 2 != 0:
                res.append(i)
            if i*i != n and (n//i) % 2 != 0:
                res.append(n//i)
        i += 1
    res = sorted(res)
    return (res[-6], len(res)) if len(res) >= 6 else 0

count = 0
n = 200000001
while count < 5:
    res = d(n)
    if res != 0:
        print(n, res)
        count += 1
    n += 1