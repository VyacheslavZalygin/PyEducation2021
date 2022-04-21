test = '10 9 4 6 12 14 2 10 12 34 31'
with open('D:/repos/PyEducation2122/AnotherEGE/27.sequences/27-3b.txt') as f:
    _, *data = [int(x) for x in f.read().strip().split()] 

last = data[0]
m = None
q = 6
for i in range(q, len(data)):
    a, b = data[i], data[i-q]
    if b > last:
        last = b
    if m == None or m < a + last:
        m = a + last

table = {}
count = 0
for i in range(q, len(data)):
    a, b = data[i], data[i-q]
    key = m-b
    if key not in table:
        table[key] = 1
    else:
        table[key] += 1
    if a in table:
        count += table[a]

print(count)