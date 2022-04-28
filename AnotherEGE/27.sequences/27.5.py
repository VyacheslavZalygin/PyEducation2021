test = '7 5 3 2 3 4 3 4 3' #5 4 5 5 5 1'
exp = 6

def symmetrical(a, b):
    return sorted(a) == sorted(b)

def equal(a, b):
    return a == b

def rotate(a, b):
    if a[1] == b[0]:    return b
    elif a[1] == b[1]:  return tuple(b[::-1])
    else:               return None

_, *data = map(int, test.split())
data = [(-1, -1)] + [(data[i], data[i+1]) for i in range(0, len(data), 2)]

sym_count = 0
m = None
curr_len = 0
# элемент 0 !!!
i = 1
while i < len(data)-1:
    curr = data[i]
    next = data[i+1]
    prev = data[i-1]
    tmp = rotate(curr, next)
    if tmp == None and curr_len == 0:
        curr == curr[::-1]
        tmp = rotate(curr, next)
    if tmp != None:
        if symmetrical(curr, prev):
            sym_count += 1
        else:
            sym_count = 0
        data[i+1] = tmp
        curr_len += 1
    else:
        if m == None or m < curr_len:
            m = curr_len+1
        curr_len = sym_count
    i += 1

if m == None or m < curr_len:
    m = curr_len+1

print(m)