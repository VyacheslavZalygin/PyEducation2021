import sys

arr = [int(x) for x in sys.stdin.read().split()]

s = set()
for e in arr:
  s.add(e)

arr = [x for x in arr if x % 2 == 0]
m = None
count = 0
for i in range(len(arr)):
  for j in range(i+1, len(arr)):
    a, b = arr[i], arr[j]
    ave = (a+b)//2
    if ave in s:
      count += 1
      if m is None or m < ave:
        m = ave
print(m, count)