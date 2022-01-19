def func(N):
    n, m = 0, 0
    while N % 2 == 0:
        N //= 2
        m += 1
    while N % 3 == 0:
        N //= 3
        n += 1
    return m % 2 == 0 and n % 2 == 1 and N == 1

a = []
for n in range(200000000, 400000001):
    print(n)
    if func(n):
        a.append(n)
        print(a)
# работает слишком долго