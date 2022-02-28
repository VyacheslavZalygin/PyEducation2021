def f(x, y, a):
  return (2*x+3*y > 30) or (x + y <= a)

for a in range(1, 100):
  isTrue = True
  for x in range(0, 1000):
    for y in range(0, 1000):
      if f(x, y, a) == 0:
        isTrue = False
        break
  if isTrue:
    print(a)
    break