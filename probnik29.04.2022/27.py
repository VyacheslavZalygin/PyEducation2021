# 14 = 7 * 2

with open('C:\\repos\\PyEducation2122\\probnik29.04.2022\\27B.txt') as f:
    _, *data = [int(x) for x in f.read().strip().split()]

with7 = None
with2 = None
with14 = None
without = None
m = None

for n in data:
    ways = [with14]

    if n % 2 == 0:
        ways.append(with7)
    if n % 7 == 0:
        ways.append(with2)
    if n % 14 == 0:
        ways.append(without)

    ways = [x for x in ways if x != None]
    for way in ways:
        if m == None or m < way*n:
            m = way*n
    
    if n % 2 == 0 and (with2 == None or with2 < n):
        with2 = n
    if n % 7 == 0 and (with7 == None or with7 < n):
        with7 = n
    if n % 14 == 0 and (with14 == None or with14 < n):
        with14 = n
    if without == None or without < n:
        without = n

print(m if m != None else 0)