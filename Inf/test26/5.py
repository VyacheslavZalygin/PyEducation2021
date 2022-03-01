import sys

_, s, *p = [int(x) for x in sys.stdin.read().split()]
special = [x for x in p if 200 <= x <= 210]
count = len(special)
res_sum = sum(special)
s -= res_sum
p = sorted([x for x in p if not(200 <= x <= 210)])

def value_or_default(a, i, d):
  return a[i] \
    if (i >= 0 and len(a) >= i+1) or (i < 0 and len(a) >= -i ) \
    else d

def f(m, p):
  if m == 0: return []
  return value_or_default(sorted(
    [[e, *f(m-e, p[:i] + p[i+1:])]for i, e in enumerate(p) if m - e >= 0],
    key=lambda arr:
      (len(arr),
       value_or_default(arr, -1, 0),
       value_or_default(arr, -2, 0))
    ), -1, [])

res = f(s, p)
print(len(res)+count, sum(res)+res_sum)
# 6 605 140 205 120 160 100 340