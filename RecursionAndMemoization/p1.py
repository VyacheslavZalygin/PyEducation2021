import sys

def f(n):
  if n == 1:
    return 1
  if n == 2:
    return 2
  if n == 3:
    return 2
  if n == 4:
    return 5
  if n == 5:
    return 5
  if n % 2 == 1:
    return f(n-1)
  return f(n-1)*2

n = [int(x) for x in sys.stdin.read().split()][0]
print(2**(n-1))