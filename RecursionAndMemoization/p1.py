import sys

table = {}

def cache(arg, func):
  if arg not in table:
    table[arg] = func(arg)
  return table[arg]

def f(n):
  if n == -1: return 0
  if n == 0 or n == 1: return 1
  return cache(n-1, f) + cache(n-2, f)

n = [int(x) for x in sys.stdin.read().split()][0]
print(f(n))

# 1 1
# 2 2
# 3 3