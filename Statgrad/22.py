def f(x):
  a, b = 1, 0
  while x > 0:
    d = x%10
    a *= d
    if d > 5:
      b += d
    x //= 10
  return a, b
# 6300 = 63 * 100 = 9 * 7 * 5 * 5 * 4
# 9 + 7
for n in range(100000):
  a, b = f(n)
  if a == 6300 and b == 19:
    print(b, n)