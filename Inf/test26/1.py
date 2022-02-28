import sys
s, *f = [int(x) for x in sys.stdin.read().split()]
f = sorted(f)
i = 0
while i < len(f) and s-f[i] >= 0:
  s -= f[i]
  i += 1
i -= 1

j = 0
if i+1 < len(f):
  while s >= 0 and i+j+1 < len(f):
    s += f[j]
    j += 1
    s -= f[i+j]
  j -= 1
print(i+1, f[i+j])