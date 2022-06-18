with open('D:\\repos\PyEducation2122\AnotherEGE\jobs.27\\27B3.txt') as f:
    _, *a = [int(x) for x in f.read().split()]

p = [(0, 0)]
k = 11
o = 5
for n in a:
    s, c = p[-1]
    p += [(s+n, c+int(n%o==0))]

count = 0
table = {}
l = 101
for s, c in p:
    key = c%k
    if key not in table:
        table[key] = 1    
    else:
        count += table[key]
        table[key] += 1
print(count)