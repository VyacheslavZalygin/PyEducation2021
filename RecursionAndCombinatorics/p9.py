import sys

def options(number, prev):
  if number == 0:
    return []
  if number < prev:
    return False
  return [x for x in range(prev, number+1)]

def sequences(number, prev):
	if number == 0: 
		return [[]]
	v = options(number, prev)
	if v == False:
		return False
	a = []
	for head in v:
		s = sequences(number-head, head)
		if s != False:
			for tail in s:
				a.append([head, *tail])
	return a

n = [int(x) for x in sys.stdin.read().split()][0]
for s in sequences(n, 1):
	print(*s)