import sys

def euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def func(a, A, n):
    a %= n
    A %= n
    b = a
    a = n
    c0 = 0
    while b != 0:
        k = -(a // b)
        a, b = b, a % b
        c0, A = A, c0 + A * k
    if c0 % n < abs(c0): c0 = c0 % n
    return c0

def try_solve(x, a, A, n):
    return (x*a)%n, A%n

def main():
    a, A, b, B, n = [int(x) for x in sys.stdin.read().split()]
    A %= n
    B %= n
    c = func(a, A, n)
    d = func(b, B, n)
    print('x = ' + str(n) + 'k + ' + str(c))
    print('x = ' + str(n) + 'k + ' + str(d))
    for k in range(-100, 100):
        x = k*n + c
        y = k*n + d
        print(x, y)

main()

