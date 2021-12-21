with open('39253.txt') as file:
    s = file.read()

a = []
for i, c in enumerate(s):
    if c == 'D':
        a.append(i)
m = -1
i = 0
while i+2 < len(a):
    if m < a[i+2] - a[i]-1:
        m = a[i+2] - a[i]-1
    i += 1
print(m)