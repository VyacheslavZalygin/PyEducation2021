import sys

div = 3
# data = []
# for string in sys.stdin.read().strip().split('\n'):
#     if string == "": continue
#     table = [None for _ in range(div)]
#     for row in string.split():
#         row = int(row)
#         key = row % div
#         if table[key] == None:
#             table[key] = row
#         else:
#             table[key] = max(row, table[key])
#     data.append(table)

# print(data)

# m_data = [None for _ in range(div)]
m_data = [None, None, 5]
data = [[6, 7, 14]]
for string in data:
    for j, m in enumerate(m_data[:]):
        for i, num in enumerate(string):
            if num == None: continue
            if m == None:
                m_data[i] = num
            else:
                k = (i+j) % div
                m_data[k] = max(m_data[k], m+num)
print(m_data)
# {0, 1, 2}
# [3, 13, 5]
# [6, 7, 14]

# [9, 10, 17] || [27, 19, 20] || [12, 19, 11]
# [9, 19, 11] || [12, 10, 20] || [27, 19, 17]
# [27, 19, 20]