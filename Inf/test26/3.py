import sys

s, *p = [x for x in sys.stdin.read().split()]
s = int(s)
p = [(int(p[i]), p[i+1]) for i in range(0, len(p), 2)]
p = sorted(p)
print(p)

def f(a):
  r = [[type, *f(a-price)] for (price, type) in p if a - price > 0]
  return max(r, key=lambda x: x.count('A'))

print(f(s))