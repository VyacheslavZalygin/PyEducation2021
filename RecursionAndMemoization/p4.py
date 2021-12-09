import sys

table = {}

def memo(k, f):
  if k not in table:
    table[k] = f(k)
  return table[k]

def count(n):
  if n == 1:
    return 1
  elif n < 1:
    return 0
  return memo(n-1, count) + memo(n-2, count) + memo(n-3, count)

b = [int(x) for x in sys.stdin.read().split()][0]
print(count(b))