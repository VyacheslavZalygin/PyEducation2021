import sys

def divisors(n): 
  i = 2
  m = n
  while i**2 <= n:
    if n % i == 0:
      if i % 10 == 8 and i != 8:
        m = min(m, i)
      if (n//i) % 10 == 8 and (n//i) != 8:
        m = min(m, n//i)
    i += 1
  return m if m != n else -1

count = 0
n = int(sys.stdin.read())
a = n+2 if n%2 == 0 else n+1
while count < 5:
  res = divisors(a)
  if res != -1:
    print(a, res)
    count += 1
  a += 2