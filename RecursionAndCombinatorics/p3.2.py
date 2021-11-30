import sys

l, n = [int(x) for x in sys.stdin.read().split()]
if l == n:
  print(1)
elif l > n:
  print(0)
