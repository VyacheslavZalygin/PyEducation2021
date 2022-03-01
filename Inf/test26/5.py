import sys

_, s, *p = [int(x) for x in sys.stdin.read().split()]
s -= sum([x for x in p if 200 <= x <= 210])
p = sorted([x for x in p if not(200 <= x <= 210)])

def f(m):
  if m == 0: return [0]
  t = [[e, *f(m-e)] for e in p if m - e >= 0]


print(f(s))