# A: 115
# B: 1365905
with open('D:\\repos\PyEducation2122\AnotherEGE\jobs.27-2\\27-8B.txt') as f:
    _, *a = [int(x) for x in f.read().split()]
a = [sorted(a[i:i+2]) for i in range(0, len(a), 2)]
diffs = [x[1]-x[0] for x in a]
mn, mx = sum([x[0] for x in a]), sum([x[1] for x in a])
print(mn, mx, mx-mn)
d = sorted([x for x in diffs if x % 5 == (mx-mn)%5])[0]
print(mx-mn-d)