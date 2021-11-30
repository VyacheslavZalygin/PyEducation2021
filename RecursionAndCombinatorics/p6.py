import sys

def sequences(free):
  if len(free) == 1:
    return [[free[0]]]
  a = [[head] for head in free]
  for head in free:
    for tail in sequences([x for x in free if x != head]):
      a.append([head, *tail])
  return a

n = [int(x) for x in sys.stdin.read().split()][0]
a = sequences([x for x in range(1, n+1)])
a.sort()
for s in a:
  print(*s)