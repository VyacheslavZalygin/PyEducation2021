import sys

def sequence(length, number):
	if length == 1:
		return [[number]]
	return [[head, *tail]
				 for head in range(1, number-length+2)
				 for tail in sequence(length-1, number-head)]

l, n = [int(x) for x in sys.stdin.read().split()]
for s in sequence(l, n):
	print(*s)

# 3 5
# 1 1 3
# 1 2 2
# 1 3 1
# 2 1 2
# 2 2 1
# 3 1 1