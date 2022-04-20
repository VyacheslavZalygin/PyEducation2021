import sys

def max_with_none(*a):
    a = [x for x in a if x != None]
    return max(a) if len(a) != 0 else None

div = 15
data = []
for string in sys.stdin.read().strip().split('\n'):
    if string == "": continue
    table = [None for _ in range(div)]
    for row in string.split():
        row = int(row)
        key = row % div
        if table[key] == None:
            table[key] = row
        else:
            table[key] = max(row, table[key])
    data.append(table)

m_data = [0] + [None for _ in range(div-1)]
for string in data:
    curr_data = [None for _ in range(div)]
    for j, m in enumerate(m_data):
        if m != None:
            for i, curr in enumerate(string):
                if curr == None: continue
                k = (i+j) % div
                curr_data[k] = max_with_none(curr_data[k], curr + m)
    m_data = curr_data
print(m_data[0] if m_data[0] != None else "NO")