import sys

def func(N):
  m, n = 0, 0
  while N % 2 == 0 and m < 12:
    N //= 2
    m += 1
  if not(2 < m < 12): return False
  while N % 3 == 0 and n < 10:
    N //= 3
    n += 1
  if not(1 < n < 10): return False
  return N == 1

a, b = [int(x) for x in sys.stdin.read().split()]
ns = []
for n in range(a, b+1):
  if n % 2 == 0 and n % 3 == 0:
    if func(n):
      ns.append(n)
if len(ns) != 0: print(*ns)
else:            print(None)