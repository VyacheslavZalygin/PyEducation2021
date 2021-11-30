import sys

def sequences(number):
	if number == 0: 
		return [[]]
	return [[head, *tail]
				 for head in [x for x in range(1, number+1)]
				 for tail in sequences(number-head)]

n = [int(x) for x in sys.stdin.read().split()][0]
for s in sequences(n):
	print(*s)