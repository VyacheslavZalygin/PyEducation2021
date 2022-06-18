# A: 13159
# B: 40799380
with open('D:\\repos\PyEducation2122\AnotherEGE\jobs.27-2\\27-5B.txt') as f:
    _, *a = [int(x) for x in f.read().split()]
a = [sorted(a[i:i+2]) for i in range(0, len(a), 2)]

k = 10
o = [0] + [None]*(k-1)
for i, ns in enumerate(a):
    if i % 1000 == 0: print(i/len(a))
    new_o = [None] * k
    for n in ns:
        for r in (x for x in o if x != None):
            key = (n+r)%k
            new_o[key] = max(new_o[key] if new_o[key] != None else 0, n+r)
    o = new_o
print(o[:5], o[6:])
print(max(o[:5] + o[6:]))