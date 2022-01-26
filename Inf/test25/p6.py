import sys

def divs(n):
  i = 2
  a = []
  while i*i < n and len(a) < 3:
    if n % i == 0:
      a.append(i)
      if n//i != i:
        a.append(n//i)
    i += 1
  if len(a) == 3: return max(a)
  return len(a)

# a, b = [int(x) for x in sys.stdin.read().split()]
# count = 0
# for n in range(a, b+1):
#   res = divs(n)
#   if res != False:
#     print(n, res)
#     count += 1
# if count == 0:
#   print(None)
print(divs(2*3*5))