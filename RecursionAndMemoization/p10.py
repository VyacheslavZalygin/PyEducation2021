import sys

T = sys.stdin.read().strip()
a = []
for i in range(len(T)+1):
    a.append((T[i:], i))

i = 1
while True:
    b = a[:]
    b.sort(key=lambda s: s[:min(i, len(s))])
    if a == b: break
    a = b
    i *= 2

print(*[p[1] for p in a])