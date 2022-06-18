with open('D:\\repos\PyEducation2122\AnotherEGE\jobs.27\\27B8.txt') as f:
    _, *a = [int(x) for x in f.read().split()]
# a = [-1, -1, 2, -3, 3, 20, 1, -1, 6, -7, 8, 23, 8, 1]

pref = [(0, 0)]
for n in a:
    s, c = pref[-1]
    pref.append((s+n, c+int(n%2==0 and n > 0)))
MAX = float('inf')
l = 1
m = -MAX
table = {}
for p, c in pref:
    if c-l in table:
        m = max(m, p-table[c-l])
    table[c] = min(table.get(c, MAX), p)
print(m)