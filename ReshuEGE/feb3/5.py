def f(n):
  n = bin(n)[2:]
  i = 1
  while i < len(n) and n[i] == '0': i += 1
  n = n[i:]
  if len(n) != 0: return int(n, 2)
  else: return 0

a = []
for n in range(100, 3001):
  a.append(n - f(n))
print(len(set(a)))