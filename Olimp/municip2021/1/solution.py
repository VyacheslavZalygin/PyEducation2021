import sys

n = int(input())
k = int(input())

k -= 1
rows2 = k // (2 * n +  1)
k %= 2 * n + 1

if k < n:
    print(2 * rows2 + 1, k + 1)
else:
    print(2 * rows2 + 2, k + 1 - n)

