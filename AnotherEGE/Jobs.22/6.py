def f(x):
    a, b = 0, 0
    while x > 0:
        if x%2 == 0:
            a += 1
        else:
            b += x%6
        x //= 6
    return a, b

for n in range(10000, 100000):
    if f(n) == (5, 11):
        print(n)
        break