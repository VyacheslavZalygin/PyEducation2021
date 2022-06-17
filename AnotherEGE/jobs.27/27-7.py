with open('D:\\repos\PyEducation2122\AnotherEGE\jobs.27\\27B7.txt') as f:
    _, *a = [int(x) for x in f.read().split()]

pref = [(0, 0)]
for n in a:
    s, c = pref[-1]
    pref.append((s+n, c+int(n%3==0)))

l = 10
m = float('inf')
table = {}
for p, c in pref:
    if c not in table:
        if c-l in table:
            m = min(m, p-table[c-l])
    table[c] = p
print(m)