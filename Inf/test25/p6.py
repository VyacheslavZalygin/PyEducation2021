import sys

def divs(n):
  i = 1
  a = []
  while i*i <= n:
    if n % i == 0:
      a.append(i)
      if i**2 != n:
        a.append(n//i)
    i += 1
  return a

a, b = [int(x) for x in sys.stdin.read().split()]
count = 0
n = int(a**0.25)
while n**4 <= b:
  if len(divs(n)) == 2:
    if n**4 >= a:
      print(n**4, n**3)
      count += 1
  n += 1
if count == 0:
  print(None)