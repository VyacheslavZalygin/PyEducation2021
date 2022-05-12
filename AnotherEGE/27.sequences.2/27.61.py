with open('D://repos/PyEducation2122/AnotherEGE/27.sequences.2/27-61b.txt') as f:
    _, *data = [int(x) for x in f.read().strip().split()]

K = 100
m = [0] + [None] * (K-1)
for n in data:
    tmp = m[:]
    for e in m:
        if e != None:
            key = (e+n) % K
            if tmp[key] == None or tmp[key] < e+n:
                tmp[key] = e+n
    if tmp[n%K] == None or tmp[n%K] < n:
        tmp[n%K] = n
    m = tmp[:]

print(m[50])