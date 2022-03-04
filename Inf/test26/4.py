import sys
from math import ceil

def discount(n): return ceil(n * 0.75)

inp = sorted([int(x) for x in sys.stdin.read().split()])
less, great = [], []
for e in inp:
  if e > 50: great.append(e)
  else: less.append(e)

great = sorted(great)
with_d, without_d = great[:len(great)//2], great[len(great)//2:]
prices = less + without_d + [discount(x) for x in with_d]

print(sum(prices), with_d[-1])