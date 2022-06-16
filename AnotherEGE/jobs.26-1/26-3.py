with open('./26-3.txt') as f:
    _, *a = [[int(y) for y in x.split()] for x in f.read().strip().split('\n')]

c = 1
a.sort(key=lambda x: (x[0], -x[1]))
for (r1, p1), (r2, p2) in zip(a, a[1:]):
    # print(r1, p1, r2, p2)
    if r1 == r2 and abs(p1-p2)==1:
        c += 1
        if c == 6:
            print(r1, p2+5)
            break
    else:
        c = 1
        