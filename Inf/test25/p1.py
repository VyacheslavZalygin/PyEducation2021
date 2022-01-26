import sys

def divisors(n):
  i = 2
  ns = []
  while i*i <= n and len(ns) < 12:
    if n % i == 0:
      ns.append(i)
      if i*i != n:
        ns.append(n//i)
    i += 1
  ns.sort()
  return ns

def M(n):
  ns = divisors(n)
  if len(ns) < 5: 
    return 0

  res = 1
  for i in ns[:5]:
    res *= i
  return res

k = int(sys.stdin.read())
result = []
N = k + 1
while len(result) < 5:
  res = M(N)
  if 0 < res < N:
    result.append(res)
  N += 1
print(*result)