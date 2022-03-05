import sys

_, s, *p = [int(x) for x in sys.stdin.read().split()]
special = [x for x in p if 200 <= x <= 210]
count = len(special)
s -= sum(special)
p = sorted([x for x in p if not(200 <= x <= 210)])

i = 0
tmp = s
while i < len(p) and tmp-p[i] >= 0:
    tmp -= p[i]
    i += 1
less, great = p[:i], p[i:]

def f(less, great, i):
    for a in great[::-1]:
        if sum(less[:i] + less[i+1:]) + a <= s:
            great.remove(a)
            great.append(less[i])
            less[i] = a
            break
    great = sorted(great)
    return less, great

for i in range(len(less)-1, -1, -1):
    less, great = f(less[:], great[:], i)

print(count + len(less), sum(special) + sum(less))
# 6 605 140 205 120 160 100 340