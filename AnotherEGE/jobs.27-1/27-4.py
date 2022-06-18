with open('D:\\repos\PyEducation2122\AnotherEGE\jobs.27\\27B4.txt') as f:
    _, *a = [int(x) for x in f.read().split()]

l = 100
k = 999
pref = [0]
for n in a:
    pref.append(pref[-1]+n)

count = 0
q = pref[:l]
ost = [0]*k
for n in pref[l:]:
    if ost[n%k] != None:
        count += ost[n%k]

    ost[q.pop(0)%k] += 1
    q.append(n)
print(count)