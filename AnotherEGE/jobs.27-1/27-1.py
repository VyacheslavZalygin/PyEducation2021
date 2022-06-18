with open('D:\\repos\PyEducation2122\AnotherEGE\jobs.27\\27-B1.txt') as f:
    _, *a = [int(x) for x in f.read().split()]

p = [(0, 0)]
k = 10
for n in a:
    s, c = p[-1]
    p += [(s+n, c+int(n%2==0))]

m_s = None
table = {}
for s, c in p:
    key = c%k
    if key not in table:
        table[key] = s    
    else:
        p_s = table[key]
        if m_s == None or m_s < s-p_s:
            m_s = s-p_s
print(m_s)