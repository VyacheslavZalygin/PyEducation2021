import sys

table = {}

def cache(func, arg):
  if arg not in table:
    table[arg] = func(arg)
  return table[arg]

def f(n):
  if n == -1: return 0
  if n == 0 or n == 1: return 1
  return cache(f, n-1) + (cache(f, n-2) if n % 3 - 1 != 1 else 1)

# n = [int(x) for x in sys.stdin.read().split()][0]
n = 6
print(f((n*3)//2))
print(table)
# 1 1
# 2 2
# 3 3