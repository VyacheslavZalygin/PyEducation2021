import sys

l, n = [int(x) for x in sys.stdin.read().split()]
res = n
for i in range(n-l+1, n):
  res *= i
print(res)