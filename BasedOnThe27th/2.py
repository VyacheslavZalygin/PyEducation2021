import sys

div = 15
data = []
for string in sys.stdin.read().strip().split('\n'):
    table = {}
    for row in string.split():
        row = int(row)
        key = row % div
        if key not in table:
            table[key] = row
        else:
            table[key] = max(row, table[key])
    data.append(table)
print(data)