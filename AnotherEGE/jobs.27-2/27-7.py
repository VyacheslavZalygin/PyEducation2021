# A: 452
# B: 3695111
def g(a):
    a = [x for x in a if x != None]
    if len(a) == 0: return None
    else:           return max(a, key=lambda x: x[0])

def ost(k, a):
    o = [(0, [])] + [None]*(k-1)
    for ns in a:
        new_os = []
        for n in ns:
            new_o = [None]*k
            for r, way in (x for x in o if x != None):
                key = (n+r)%k
                new_o[key] = (max(new_o[key] if new_o[key] != None else 0, n+r), way+[n])
            new_os.append(new_o)
        o = [g(x) for x in zip(*new_os)]
    return o

with open('D:\\repos\PyEducation2122\AnotherEGE\jobs.27-2\\27-7B.txt') as f:
    _, *a = [int(x) for x in f.read().split()]
a = [sorted(a[i:i+2]) for i in range(0, len(a), 2)]

for e, x in ost(5, a)[1:]:
    s = 0
    for i in range(len(x)):
        if a[i][0] == x[i]:
            s += a[i][1]
        else:
            s += a[i][0]
    if s % 3 != 0:
        print(e, s)
    else:
        print(e, s, 'NO')
