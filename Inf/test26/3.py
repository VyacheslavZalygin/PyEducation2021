import sys

s, *p = [x for x in sys.stdin.read().split()]
s = int(s)
p = [(int(p[i]), int(p[i+1]), p[i+2]) for i in range(0, len(p), 3)]
table = { 'A': [], 'B': []}
for (price, amount, t) in p:
  table[t].append([price, amount])

def B(): return table['B']
def A(): return table['A']

table['A'].sort()
table['B'].sort()
while B() != [] and s-B()[0][0] > 0:
  s -= B()[0][0]
  B()[0][1] -= 1
  if B()[0][1] == 0:
    B().pop(0)

count = 0
while A() != [] and s-A()[0][0] > 0:
  s -= A()[0][0]
  A()[0][1] -= 1
  count += 1
  if A()[0][1] == 0:
    A().pop(0)
print(count, s)