import sys

def sequence(length, number):
	if length == 1:
		return 1
	if length < 1:
		return 0
	res = 0
	for head in range(1, number-length+2):
		res += sequence(length-1, number-head)
	return res

l, n = [int(x) for x in sys.stdin.read().split()]
print(sequence(l, n))

# 3 5
# 1 1 3
# 1 2 2
# 1 3 1
# 2 1 2
# 2 2 1
# 3 1 1
# 6