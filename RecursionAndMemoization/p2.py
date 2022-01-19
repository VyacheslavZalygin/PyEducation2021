import sys

table_f = {}
table_g = {}

def cache(func, arg, n):
  if n == 1:
    table = table_f
  if n == 2:
    table = table_g

  if arg not in table:
    table[arg] = func(arg)
  return table[arg]

def f(n):
  if n >= 2:
    return cache(f, n-2, 1) + 2*cache(g, n-1, 2)
  elif n >= 0:
    return 1
  else:
    return 0

def g(n):
  if n >= 3:
    return cache(f, n-1, 1) + cache(g, n-2, 2)
  elif n == 1:
    return 1
  else:
    return 0

n = [int(x) for x in sys.stdin.read().split()][0]
print(f(n) if n % 2 == 0 else 0)