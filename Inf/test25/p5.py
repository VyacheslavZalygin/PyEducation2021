import sys

def divs(n):
  i = 1
  a = []
  while i*i <= n and len(a) < 6:
    if n % i == 0:
      if i % 2 == 1:
        a.append(i)
      if i*i != n and (n//i) % 2 == 1:
        a.append(n//i)
    i += 1
  return a

def is_prime(n):
  return len(divs(n)) == 2

a, b = [int(x) for x in sys.stdin.read().split()]
res = []
for n in range(a, b+1):
  n_t = n
  while n_t % 2 == 0:
    n_t //= 2 
  n_t = n_t ** 0.25
  if n_t == int(n_t):
    if is_prime(n_t): 
      res.append((n))
if len(res) != 0:
  print(*res)
else:
  print(None)