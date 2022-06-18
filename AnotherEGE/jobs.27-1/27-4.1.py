f = open('27A4.txt')
n = int(f.readline())
q = []
l = 100
s = 0
k = 999
q.append(0)
for i in range(l):
    x = int(f.readline())
    s += x
    q.append(s)

count = 0
p = [0]*k
for i in range(n-l):
    x = int(f.readline())
    s += x
    count += p[s%k]

    p[q.pop(0)%k] += 1
    q.append(s)
print(count)