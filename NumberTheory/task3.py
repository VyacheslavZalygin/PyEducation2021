import sys

def main():
    a, b, n = [int(x) for x in sys.stdin.read().split()]
    print(pow(a, b, n) % n)

def pow(a, b, n):
    if b == 0:
        return 1
    if b == 1:
        return a % n
    if not b % 2:
        return pow(((a%n) * (a%n))%n, b // 2, n)
    else:
        return ((a%n) * (pow(a, b-1, n)%n))%n

main()