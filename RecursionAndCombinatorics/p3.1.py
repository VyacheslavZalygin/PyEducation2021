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
for s in sequences(l, {x for x in range(1, n + 1)}):
  print(*s)