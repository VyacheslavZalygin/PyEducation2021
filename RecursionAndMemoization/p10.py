import sys

T = sys.stdin.read().strip()
a = []
for i in range(len(T)+1):
    a.append((T[i:], i))
a.sort()
print(*[p[1] for p in a])