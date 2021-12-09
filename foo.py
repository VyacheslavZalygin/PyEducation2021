def func(x): 
  y = 0
  z = 1
  while x>0:
    y += 1
    z = z * (x % 15)
    x //= 15
  return y, x+z

for n in range(1000000, 0, -1):
  r1, r2 = func(n)
  print(r1, r2)
  if r1 == 4 and r2 == 60:
    print(n)
    break