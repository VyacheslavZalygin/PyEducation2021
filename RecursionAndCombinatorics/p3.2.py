import sys

def fac(n):
  return n * fac(n-1) if n > 0 else 1

k, n = [int(x) for x in sys.stdin.read().split()]
print(fac(n)//(fac(n-k)*fac(k)))