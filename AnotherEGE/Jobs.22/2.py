def f(x):
    l, m, r = 0, 0, 0
    while x > 0:
        r = r*10 + x % 10
        x //= 10
        if x <= r:
            m += 1
        else:
            l += x%10
    return l, m

for n in range(1000000, -1, -1):
    if f(n) == (14, 3) and '0' not in str(n):
        print(n)
        break