import sys

def div(a, e = None):
  return {x for x in a if e is not None and x > e}

def sequences(length, free):
  if length == 0:
    return [[]]
  return [[head, *tail]
          for head in free
          for tail in sequences(length - 1, div(free, head))]

l, n = [int(x) for x in sys.stdin.read().split()]
a = sequences(l, {x for x in range(1, n + 1)})
for s in a:
  print(*s)
print(len(a))

#    3 4 5  6
# 1: 3 4 5  6
# 2: 3 6 10 15
# 3: 1 4 10 20
# 4: 0 1 5  15