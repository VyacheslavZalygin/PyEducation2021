def f(x):
    a = 0
    b = 1
    while x > 0:
        a += 1
        b *= x % 10
        x //= 10
    return a, b

for x in range(1000, 1, -1):
    if f(x) == (2, 72):
        print(x)
        break