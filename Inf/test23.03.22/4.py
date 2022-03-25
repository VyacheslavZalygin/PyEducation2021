def to(n, i):
  res = []
  while n > 0:
    res.append(str(n % i))
    n //= i
  return ''.join(reversed(res))

def f(n):
  o = n % 3
  n = to(n, 3)
  n += str(o)
  return int(n, 3)

d = set()
for n in range(5000):
  r = f(n)
  if len(str(r)) == 3:
    d.add(r)
print(min(d))