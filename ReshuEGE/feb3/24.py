with open('24.txt') as f:
  arr = f.read().split('A')

def f(s):
  e = 0
  for l in s:
    if l == 'E':
      e += 1
  return len(s) if e >= 3 else 0

m = 0
for s in arr:
  m = max(m, f(s))
print(m)