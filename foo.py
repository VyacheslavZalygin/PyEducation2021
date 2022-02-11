def f(n, i):
  res = ""
  while n > 0:
    res = str(n % i) + res
    n //= i
  return res

a = ""
for n in range(15, 25):
  a += str(f(n, 7)) + " "

print(a)
print(a.count('3'))