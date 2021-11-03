import sys

x, y = [int(i) for i in sys.stdin.read().split()]
if x % 2 != y % 2:
  print(-1)
elif x == y:
  print(0)
elif y >= -x +2: # передняя часть
  o = 'H'
  if x < y:
    x, y = y, x
    o = 'V'
  p = (x - y) // 2 + y
  print(1)
  print(p, p, o)
elif y <= x-2: # нижняя часть
  print(2)
  print(x, x, 'H')
  x1 = (x-y) // 2 + x
  y1 = (x+y) // 2
  print(x1, y1, 'V')
elif y >= x+2: # верхняя часть
  print(2)
  print(y, y, 'V')
  x1 = y - (y-x) // 2
  y1 = y + (y-x) // 2
  print(x1, y1, 'H')
else:
  print(-1)



