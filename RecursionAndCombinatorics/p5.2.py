import sys

def sequence(length, number, prev = 1):
	if length == 1:
		return 1
	elif length == 0: 
		return 0
	res = 0
	for head in [x for x in range(prev, number//length+1)]:
		res += sequence(length-1, number-head, head)
	return res

l, n = [int(x) for x in sys.stdin.read().split()]
print(sequence(l, n))