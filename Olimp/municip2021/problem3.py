import sys

def get(s, i, n):
  if i < (n-1)*len(s):
    if len(s) <= i:
      return True, s[i%len(s)], True
    return False, s[i], True
  return False, 0, False

t, s, n = [x for x in sys.stdin.read().split()]
n = int(n)
res, res1 = 0, 0

for i in range(len(s)):
  if s[i] == t[0]:
    c = True
    c1 = False
    for j in range(len(t)):
      ci, g, cf = get(s, i+j, n)
      if ci:
        c1 = True
      if g != t[j] or not cf:
        c = False
        break
    if c and not c1:
      res += 1
    elif c and c1:
      res1 += 1
print(res*n+res1*(n-1))