import sys

_, s, *p = [int(x) for x in sys.stdin.read().split()]
special = [x for x in p if 200 <= x <= 210]
count = len(special)
res_sum = sum(special)
s -= res_sum
p = sorted([x for x in p if not(200 <= x <= 210)])

i = 0
while i < len(p) and s-p[i] >= 0:
  s -= p[i]
  res_sum += p[i]
  count += 1
  i += 1
i -= 1

j = 0
if i+1 < len(p):
  while s >= 0 and i+j+1 < len(p):
    s += p[j]
    res_sum -= p[j]
    j += 1
    s -= p[i + j]
    res_sum += p[i+j]
  j -= 1
print(count, res_sum)
# 6 605 140 205 120 160 100 340