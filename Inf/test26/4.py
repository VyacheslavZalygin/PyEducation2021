import sys
from math import ceil

def discount(n): return ceil(n * 0.75)

inp = sorted([int(x) for x in sys.stdin.read().split()])
less, great = [], []
for e in inp:
  if e > 50: great.append(e)
  else: less.append(e)

prices = less
n = 1
m = 0
while len(great) != 0:
  if n % 2 == 1:
    prices.append(great.pop(-1))
  else:
    e = great.pop(0)
    m = max(m, e)
    prices.append(discount(e))
  n += 1
print(sum(prices), m)