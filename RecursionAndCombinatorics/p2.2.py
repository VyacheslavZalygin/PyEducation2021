import sys

l, n = [int(x) for x in sys.stdin.read().split()]
res = 1
for i in range(n-l+1, n+1):
  res *= i
print(res)