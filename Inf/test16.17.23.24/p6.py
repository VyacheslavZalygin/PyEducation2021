import sys

a = [int(x) for x in sys.stdin.read().split()]
count = 0
max_diff = None
for i in range(len(a)):
    for j in range(i+1, len(a)):
        n1, n2 = a[i], a[j]
        if n2 > n1: n1, n2 = n2, n1
        if (n1-n2) % 36 == 0 and (n1 % 13 == 0 or n2 % 13 == 0):
            count += 1
            if max_diff == None or n1-n2 > max_diff:
                max_diff = n1-n2

print(count, max_diff)