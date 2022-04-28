import sys

div = 15
data = [[int(x) for x in string.split()] for string in sys.stdin.read().split("\n") if string != ""]

m_data = [{0: 0}] + [{} for _ in range(div-1)]
for string in data:
    curr_data = [{} for _ in range(div)]

    for old_table in m_data:
        for e in old_table:
            s = old_table[e]
            for curr in string:
                even_count = e
                k = (curr+s) % div
                new_table = curr_data[k]
                if curr % 2 == 0: even_count += 1
                if even_count not in new_table or new_table[even_count] < curr+s:
                    new_table[even_count] = curr+s
    m_data = curr_data

# print(m_data[0])

res = []
for even in m_data[0]:
    odd = len(data)-even
    s = m_data[0][even]
    if (even > odd and s % 2 == 0) or (odd > even and s % 2 == 1):
        res.append(s)

if len(res) != 0:
    print(max(res))
else:
    print('NO')