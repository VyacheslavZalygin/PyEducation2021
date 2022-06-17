def f(x):
    a = 0
    b = 1
    while x > 0:
        if x % 2 > 0:
            a += 1
        else:
            b += x % 5
        x //= 5
    return a, b

for n in range(5000):
    if f(n) == (2, 9):
        print(n)