import sys

table = {}

def memo(k, f):
  if k not in table:
    table[k] = f(*k)
  return table[k]

def count(s, n):
  if s == n:
    return 1
  elif s > n:
    return 0
  return memo((s+1, n), count) + memo((s+2, n), count) + memo((s*3, n), count)

b = [int(x) for x in sys.stdin.read().split()][0]
print(count(1, b))