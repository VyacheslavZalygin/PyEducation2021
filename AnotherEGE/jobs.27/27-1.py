with open('./27-A1.txt') as f:
    _, *a = [int(x) for x in f.read().split()]

e = 0
p = [(0, 0)]
for n in a:
    p += [(p[-1][0]+n, p[-1][1]+n%2==0)]
print(p)