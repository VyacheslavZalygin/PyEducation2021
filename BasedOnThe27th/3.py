import sys

div = 15
data = [[int(x) for x in string.split()] for string in sys.stdin.read().split("\n") if string != ""]

m_data = [[(0, 0), (0, 0)]] + [[None, None] for _ in range(div-1)]
for string in data:
    curr_data = [[None, None] for _ in range(div)]
    for m in m_data:
        for pair in m:
            if pair != None:
                even_count, s = pair 
                for curr in string:
                    even_count_curr = even_count
                    k = (curr+s) % div
                    if curr % 2 == 0: even_count_curr += 1
                    if curr_data[k][even_count_curr%2] == None or curr_data[k][even_count_curr%2][1] < curr+s:
                        curr_data[k][even_count_curr%2] = (even_count_curr, curr + s)
    m_data = curr_data

# print(m_data[0])

choice = []
if m_data[0][0] != None and m_data[0][0][0] > len(data)//2:
    choice.append(m_data[0][0][1])
if m_data[0][1] != None and m_data[0][1][0] > len(data)//2:
    choice.append(m_data[0][1][1])
if len(choice) != 0:
    print(max(choice))
else:
    print("NO")
