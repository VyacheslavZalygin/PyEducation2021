test = '6 2 5 4 6 5 9 6 8 1 7 2 6'
with open('D:/repos/PyEducation2122/AnotherEGE/27.sequences/27-4b.txt') as f:
    _, *data = [int(x) for x in f.read().strip().split()] 
data = [sorted([data[i], data[i+1]]) for i in range(0, len(data), 2)]

s = 0
odd = 0
for a, b in data:
    if b % 2 == 1:
        odd += 1
    s += b

if odd % 2 == 0:
    print(':D')
    print(s)
    exit()

delta = None
for a, b in data:
    if (a + b) % 2 == 0:
        continue

    if delta == None or delta > b-a:
        delta = b-a

print(s-delta)