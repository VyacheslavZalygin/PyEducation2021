def divs(n):
  i = 1
  res = []
  while i**2 <= n:
    if n % i == 0:
      res.append(i)
      if i**2 != n:
        res.append(n//i)
    i += 1
  res.sort()
  return res[:-1]

def m(n):
  div = divs(n)
  return div[-1]+div[-2] if len(div) >= 2 else 0

n = 10000001
count = 0
while count < 5:
  if 0 < m(n) < 10000:
    print(n, m(n))
    count += 1
  n += 1