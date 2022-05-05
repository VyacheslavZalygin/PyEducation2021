def max_with_none(*a):
    a = [x for x in a if x != None]
    return max(a) if len(a) != 0 else None

def func(div, data):
    m_data = [0] + [None for _ in range(div-1)]
    for string in data:
        curr_data = [None for _ in range(div)]
        for m in m_data:
            if m != None:
                for curr in string:
                    if curr == None: continue
                    k = (curr+m) % div
                    curr_data[k] = max_with_none(curr_data[k], curr + m)
        m_data = curr_data
    return m_data

div1 = 7
div2 = 10
with open('D:/repos/PyEducation2122/AnotherEGE/27.sequences/27-64b.txt') as f:
    data = [[int(x) for x in string.split()] for string in f.read().strip().split("\n")[1:]]

res1 = func(div1, data)
res2 = func(div2, data) 
print(res1[3], res1)
print(res2[5], res2)