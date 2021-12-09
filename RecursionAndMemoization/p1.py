import sys

def f(n):
  if n == 1:
    return 1
  return f(n-1)*2

n = [int(x) for x in sys.stdin.read().split()][0]
print(2**(n-1))