import sys

data = [int(x) for x in sys.stdin.read().split()]

prefixes = [(0, 0)]
div = 5

for num in data:
    count, s = prefixes[-1]
    prefixes.append((count + num%2, s+num))

m = None
table = {}
for count, s in prefixes:
    key = count % div
    if key not in table:
        table[key] = s
    else:
        s -= table[key]
        if m == None or m < s:
            m = s

# print(table)
# print(prefixes)
print(m if m != None else 0)