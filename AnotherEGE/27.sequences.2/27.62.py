with open('D://repos/PyEducation2122/AnotherEGE/27.sequences.2/27-62b.txt') as f:
    _, *data = [int(x) for x in f.read().strip().split()]

# data = [int(x) for x in '1 4 7 3 20 5'.split()]

table = set(data)
data = sorted(data)

m = 0
for n in data:
    for k in range(1, 101):
        tmp = n
        curr = 0
        while tmp in table:
            curr += 1
            tmp += k
        m = max(m, curr)

print(m)
