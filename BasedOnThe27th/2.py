import sys

def max_with_none(*a):
    a = [x for x in a if x != None]
    return max(a) if len(a) != 0 else None

div = 15
data = [[int(x) for x in string.split()] for string in sys.stdin.read().split("\n") if string != ""]

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
print(m_data[0] if m_data[0] != None else "NO")