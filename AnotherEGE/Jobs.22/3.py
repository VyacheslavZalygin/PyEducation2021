def f(x):
    a = 5*x + 345
    b = 5*x - 807
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

for n in range(200, 1000):
    if f(n) == 96:
        print(n)
        break