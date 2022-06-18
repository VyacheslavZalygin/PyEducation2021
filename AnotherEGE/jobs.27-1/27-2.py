with open('27_B2.txt') as f:
    _, *a = [int(x) for x in f.read().split()]

p = [0]
k = 43
for n in a:
    p += [p[-1]+n]

m_s = None
m_l = None
table = {}
for i, s in enumerate(p):
    key = s%k
    if key not in table:
        table[key] = (i, s)
    else:
        j, p_s = table[key]
        if m_s == None or m_s < s-p_s:
            m_s = s-p_s
            m_l = i-j
        if m_s == s-p_s and m_l > i-j:
            m_l = i-j
print(m_l)