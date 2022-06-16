with open('./26-2.txt') as f:
    _, *data = [int(x) for x in f.read().split()]

data = sorted([tuple(data[i:i+2]) for i in range(0, len(data), 2)], key=lambda x: (-x[0], x[1]))

m_p = m_r = None
c = 1
for (r1, p1), (r2, p2) in zip(data, data[1:]):
    if r1 == r2:
        if p2-p1 == 1:
            c += 1
        else:
            if m_p == None or m_p < c:
                m_p = c
                m_r = r1
            c = 1
    else:
        if m_p == None or m_p < c:
            m_p = c
            m_r = r1
        c = 1
print(m_r, m_p)