import sys

def euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solve(b, B, n):
    # nod = euclidean(b, n)
    # if B % nod != 0:
    #     return False
    # mod = n
    # b //= nod
    # B //= nod
    # n //= nod
    b %= n
    B %= n
    a = n
    A = 0
    while b != 0:
        k = (a // b)
        a, b = b, a % b
        A, B = B, A - k * B
    return A%n # { x%mod for x in range(A, mod, n) }

def main():
    a, A, b, B = [int(x) for x in sys.stdin.read().split()]
    # x =a= A; x = ay + A
    # x =b= B; x = bz + B
    # ay + A = bz + B
    # ay = B - A + bz
    # ay =b= B - A
    m = a*b
    n = a
    C = B - A
    nod = euclidean(a, b)
    if C % nod != 0:
        return
    C //= nod
    a //= nod
    b //= nod
    c = solve(a, C, b)
    # y =b= c
    # y = bk+c
    # x = a(bk+c)+A
    # x = abk+(ac+A)
    k = n*b
    res = {x%m for x in range(n*c+A, m, k)}
    res = sorted(res)
    if len(res) != 0:
        print(*res)

main()