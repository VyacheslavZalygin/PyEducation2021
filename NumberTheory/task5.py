import sys

def solve(a, A, b, B, n):
    while b != 0:
        k = (a // b)
        a, b = b, a % b
        A, B = B, A - k * B
    return A%n

def main():
    a, A, b, B = [int(x) for x in sys.stdin.read().split()]
    A %= a
    B %= b
    c = solve(b, A*b, a, B*a, a*b)
    print(c)

main()