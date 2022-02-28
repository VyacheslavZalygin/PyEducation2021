def f(n, i):
  res = []
  while n > 0:
    res.append(n % i)
    n //= i
  res.reverse()
  return res

for i in range(11, 1000):
  if f(87, i)[-1] == 2:
    print(i, f(87, i))