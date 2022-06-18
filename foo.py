with open('D:\\repos\PyEducation2122\\26.txt') as f:
    _, m, *data = [x for x in f.read().split()]
    m = int(m)
    a, b = [], []
    for i in range(0, len(data), 2):
        cost, type = data[i:i+2]
        cost = int(cost)
        if type=='A':   a.append(cost)
        else:           b.append(cost)
    a.sort()
    b.sort()
    i = -1
    while m > 0:
        i += 1
        m -= a[i]
    m += a[i]
    i -= 1
    print(b)
    print(i, m)