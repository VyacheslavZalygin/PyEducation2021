import sys

def solve(a, A, b, B, n):
    while b != 0:
        k = (a // b)
        a, b = b, a % b
        A, B = B, A - k * B
    return A%n

def is_fits(c, a, A, n):
    return (c*a)%n == A%n

def main():
    a, A, b, B, n = [int(x) for x in sys.stdin.read().split()]
    a %= n
    A %= n
    b %= n
    B %= n
    c = solve(a, A, b, B, n)
    if is_fits(c, a, A, n) and is_fits(c, b, B, n):
        print(c)

main()

