import sys

def pythagorean(a, b, c):
    return a**2 + b**2 == c**2

a = [int(x) for x in sys.stdin.read().split()]
a = [(a[i-1], a[i], a[i+1]) for i in range(1, len(a)-1)]
count = 0
max_sum = 0
for k, m, l in a:
    if pythagorean(k, m, l) or pythagorean(k, l, m) or pythagorean(m, l, k):
        count += 1
        if k+m+l > max_sum:
            max_sum = k+m+l
print(count, max_sum)