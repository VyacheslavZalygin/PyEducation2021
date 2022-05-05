test = '4\n7 3\n4 11\n9 12\n15 9' # 26, 13, 39

def max_with_none(*a):
    a = [x for x in a if x != None]
    return max(a) if len(a) != 0 else None

with open('D:/repos/PyEducation2122/AnotherEGE/27.sequences/27-69b.txt') as f:
    data = [[int(x) for x in string.split()] for string in f.read().strip().split("\n")[1:]]

data = [sorted((a, b)) for a, b in data if a % 2 == 1]

div = 4
m_data = [(0, 0)] + [None for _ in range(div-1)]
for string in data:
    curr_data = [None for _ in range(div)]
    for m in m_data:
        if m != None:
            if string == None: continue
            k = (string[0]+m[0]) % 2 + ((string[1] + m[1]) % 2)*2
            curr_data[k] = max_with_none(curr_data[k], (string[0] + m[0], string[1] + m[1]))
    for i in range(div):
        if curr_data[i] != None and (m_data[i] == None or sum(m_data[i]) < sum(curr_data[i])):
            m_data[i] = curr_data[i]  

print(m_data[2], m_data)
print(sum(m_data[2]))