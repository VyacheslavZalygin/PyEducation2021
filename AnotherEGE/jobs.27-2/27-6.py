# A: 6687
# B: 20191263
with open('D:\\repos\PyEducation2122\AnotherEGE\jobs.27-2\\27-6A.txt') as f:
    _, *a = [int(x) for x in f.read().split()]
a = [sorted(a[i:i+2]) for i in range(0, len(a), 2)]

k = 8**3
o = [0] + [None]*(k-1)
for ns in a:
    new_o = [None] * k
    for n in ns:
        for r in (x for x in o if x != None):
            key = (n+r)%k
            new_o[key] = min(\
                new_o[key] if new_o[key] != None else float('inf'), \
                n+r)
    o = new_o
print(o)
print(o[31])