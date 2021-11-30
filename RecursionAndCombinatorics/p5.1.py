import sys

def options(length, number, prev):
  if length == 1:
    return [number]
  return [x for x in range(prev, number//length+1)]

def sequence(length, number, prev = 1):
	if length == 0: 
		return [[]]
	return [[head, *tail]
		for head in options(length, number, prev)
		for tail in sequence(length-1, number-head, head)]

l, n = [int(x) for x in sys.stdin.read().split()]
for s in sequence(l, n):
	print(*s)