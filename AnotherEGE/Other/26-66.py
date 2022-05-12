from turtle import st


with open('D://repos/PyEducation2122/AnotherEGE/Other/26-66.txt') as f:
    n, start = [int(x) for x in f.readline().split()]
    delta = 24 * 60 * 60 * 1000
    end = start + delta

    data = [0] * (delta + 1)
    for _ in range(n):
        s, e = map(int, f.readline().split())
        if s < start:
            data[0] += 1
        elif s <= end:
            data[s-start] += 1
        
        if start <= e <= end:
            data[e-start] -= 1

    curr = 0
    m = 0
    time = 0
    for i, update in enumerate(data):
        if update != 0:
            if curr > m:
                m = curr
            curr += update
    
        if i % int(len(data) * 0.005) == 0:
            print(int(i/len(data) * 1000)/10)
    
    curr = 0
    for i, update in enumerate(data):
        curr += update
        if curr == m:
            time += 1

        if i % int(len(data) * 0.005) == 0:
            print(int(i/len(data) * 1000)/10)
    
    print(m, time)