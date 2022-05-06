with open('C:\\repos\\PyEducation2122\\probnik29.04.2022\\24.txt') as f:
    data = f.read().strip()

data = data.replace('AB', '*')
curr = 0
m = None
for e in data:
    if e == '*':
        curr += 2
    elif curr > 0 and e == 'A':
        curr += 1
        if m == None or m < curr:
            m = curr
        curr = 0
    else:
        if m == None or m < curr:
            m = curr
        curr = 0

print(m)