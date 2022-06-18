with open('D:\\repos\PyEducation2122\AnotherEGE\jobs.27\\27B6.txt') as f:
    _, *a = [int(x) for x in f.read().split()]
# a = [17, 22, 11, 67, 14, 117]

pref = [(0, 0)]
for i, n in enumerate(a, start=1):
    pref += [(pref[-1][0]+n, i)]

k = 39
l = 20
count = 0
ost = [[] for _ in range(k)]
for p, i in pref:
    o = ost[p%k]
    while len(o) > 0 and i-o[0] > l:
        o.pop(0)
    count += len(o)
    o.append(i)
print(count)