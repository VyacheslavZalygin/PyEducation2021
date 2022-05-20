with open('D://repos/PyEducation2122/AnotherEGE/26/26-1.txt') as f:
    k, n = map(int, f.readline().split())
    ways = {x: (int(f.readline()), []) for x in range(k)}
    students = [tuple(map(int, f.readline().split())) for _ in range(n)]

    for c, i in students:
        ways[i][1].append(c)

    res = 0
    m = None
    d = None
    for key in ways:
        students = sorted(ways[key][1], reverse=True)
        count = ways[key][0]
        if len(students) <= count:
            res += len(students)
        else:
            res += count
        
        if m == None or len(students)/count > m:
            m = len(students)/count
            d = students[count-1]
    
    print(res, d, m)