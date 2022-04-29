with open('C:\\repos\\PyEducation2122\\probnik29.04.2022\\17.txt') as f:
    data = [int(x) for x in f.read().strip().split()]

data = [(data[i], data[i+1]) for i in range(len(data)-1)]

count = 0
m = None

for a, b in data:
    if (a * b) % 15 == 0 and (a + b) % 7 == 0:
        count += 1
        if m == None or m < a + b:
            m = a + b

print(count, m)