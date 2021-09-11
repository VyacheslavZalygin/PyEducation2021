import sys

def euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solve(b, B, n):
    nod = euclidean(b, n)
    if B % nod != 0:
        return False
    b //= nod
    B //= nod
    n //= nod
    a = n
    A = 0
    b %= n
    B %= n
    while b != 0:
        k = (a // b)
        a, b = b, a % b
        A, B = B, A - k * B
    return A%n

def main():
    a, A, b, B, n = [int(x) for x in sys.stdin.read().split()]
    c = solve(a, A, n)
    d = solve(b, B, n)
    if c is False or d is False:
        return
    if c == d:
        print(c)

main()