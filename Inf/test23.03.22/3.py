def f(n):
  n = bin(n)[2:]
  n += str(sum([int(x) for x in n]) % 2)
  n += str(sum([int(x) for x in n]) % 2)
  return int(n, 2)

r = set()
for n in range(500):
  a = f(n)
  if a < 100:
    r.add(a)
print(max(r))