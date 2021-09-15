import sys

def euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solve(b, B, n):
    nod = euclidean(b, n)
    if B % nod != 0:
        return False
    mod = n
    b //= nod
    B //= nod
    n //= nod
    b %= n
    B %= n
    a = n
    A = 0
    while b != 0:
        k = (a // b)
        a, b = b, a % b
        A, B = B, A - k * B
    return { x%mod for x in range(A, mod, n)}

def main():
    a, A, b, B, n = [int(x) for x in sys.stdin.read().split()]
    c = solve(a, A, n)
    d = solve(b, B, n)
    if c is False or d is False:
        return
    i = c & d
    if len(i) == 0:
        return
    print(*i)

main()