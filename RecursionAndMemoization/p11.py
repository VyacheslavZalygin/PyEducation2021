import sys

T = sys.stdin.read().strip()
a = []
for i in range(len(T)+1):
    a.append(T[i:])

while True:
    b = a[:]
    b.sort(key=lambda s: )
    if a == b: break
    a = b
    i *= 2

print(a)