test = '6 9 4 5 6 14 2'
with open('D:/repos/PyEducation2122/AnotherEGE/27.sequences/27-1b.txt') as f:
    _, *data = [int(x) for x in f.read().strip().split()] 

# 21 = 7 * 3
without_max = None
with7_max = None
with3_max = None
with37_max = None

def max_with_None(*collection):
    collection = [x for x in collection if x != None]
    return max(collection) if len(collection) != 0 else None

m = None
for n in data:    
    prev_maxes = [with37_max]
    if n % 3 == 0:
        prev_maxes.append(with7_max)
    if n % 7 == 0:
        prev_maxes.append(with3_max)
    if n % 3 == 0 and n % 7 == 0:
        prev_maxes.append(without_max)

    without_max = max_with_None(without_max, n)
    if n % 3 == 0:
        with3_max = max_with_None(with3_max, n)
    if n % 7 == 0:
        with7_max = max_with_None(with7_max, n)
    if n % 3 == 0 and n % 7 == 0:
        with37_max = max_with_None(with37_max, n)
    
    current_max = [x*n for x in prev_maxes if x != None]
    if len(current_max) == 0:
        current_max = None
    else:
        current_max = max(current_max)
    
    m = max_with_None(m, current_max)

print(m)