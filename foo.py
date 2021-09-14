def foo(n):
    b = ''
    while n != 0:
        b += str(n % 2)
        n //= 2
    b += str(sum([int(x) for x in b]) % 2)
    b += str(sum([int(x) for x in b]) % 2)
    a = 1
    res = 0
    while len(b) != 0:
        res += int(b[0]) * a
        a *= 2
        b = b[1:]
    return res

def task5():
    for n in range(0, 100):
        r = foo(n)
        print(n, r)
        if r > 77:
            exit(0)

def task6(s):
    s = s // 10
    n = 1
    while s < 51:
        s = s + 5
        n = n * 2
    return n

# for t in range(0, 100000):
#     r = task6(t)
#     print(t, r)
task5()
