import sys

def divisors(n): 
  i = 2
  while i*i <= n:
    if n % i == 0:
      if i % 10 == 8 and i != 8:
        return i
      i_2 = n//i
      if i_2 % 10 == 8 and i_2 != 8:
        return i_2
    i += 1
  return -1  

n = 1500000000#int(sys.stdin.read())
count = 0
a = n+2 if n%2 == 0 else n+1
while count < 5:
  res = divisors(a)
  if res != -1:
    print(a, res)
    count += 1
  a += 2
# print(divisors(1500000008))