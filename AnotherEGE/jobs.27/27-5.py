with open('D:\\repos\PyEducation2122\AnotherEGE\jobs.27\\27B5.txt') as f:
    _, *a = [int(x) for x in f.read().split()]

l = 50
k = 777
pref = [0]
for n in a:
    pref.append(pref[-1]+n)

m_s = float('inf')
q = pref[:l]
ost = [None]*k
for n in pref[l:]:
    if ost[n%k] != None:
        if m_s > n-ost[n%k]:
            m_s = n-ost[n%k]

    w = q.pop(0)
    ost[w%k] = w
    q.append(n)
print(m_s)