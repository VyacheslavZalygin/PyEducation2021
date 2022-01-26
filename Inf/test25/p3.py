import sys

def divisors(n):
    d = 1
    ds = []
    while d*d <= n:
        if n % d == 0:
            ds.append(d)
            if d*d != n:
                ds.append(n//d)
        d += 1
    return ds
  
def is_prime(n):
  return len(divisors(n)) == 2

a, b = [int(x) for x in sys.stdin.read().split()]
ns = []
for n in range(a, b+1):
  if n % 2 == 0:
    i = (n/2)**0.5
    if i == int(i):
      if is_prime(i):
        ns.append(n)
if len(ns) != 0: print(*ns)
else:            print(None)