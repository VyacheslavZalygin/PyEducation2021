import sys

div = 15
data = [[int(x) for x in string.split()] for string in sys.stdin.read().split("\n") if string != ""]

m_data = [{0: 0}] + [{} for _ in range(div-1)]
for string in data:
    curr_data = [{} for _ in range(div)]
    # for m in m_data:
    #     for pair in m:
    #         if pair != None:
    #             e, s = pair 
    #             for curr in string:
    #                 even_count = e
    #                 k = (curr+s) % div
    #                 if curr % 2 == 0: even_count += 1
    #                 if curr_data[k][even_count%2] == None or curr_data[k][even_count%2][1] < curr+s:
    #                     curr_data[k][even_count%2] = (even_count, curr + s)

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

res = [m_data[0][x] for x in m_data[0] if x > len(data)//2]
if len(res) != 0:
    print(max(res))
else:
    print("NO")

# 1 2 3
# 12 29
# 1 16