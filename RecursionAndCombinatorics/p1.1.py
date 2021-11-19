def sequences(length, n):
  if length == 0:
    return []
  if length == 1:
    return [[head]
            for head in range(1, n+1)]
  return [[head, *tail]
          for head in range(1, n+1)
          for tail in sequences(length-1, n)]

import sys
k, n = [int(x) for x in sys.stdin.read().split()]
for s in sequences(k, n):
  print(*s)