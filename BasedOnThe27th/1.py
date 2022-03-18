import sys
from heapq import heappush, heappop

# запоминаем наибольшие числа с разделение на типы множителей, съедаем число и думаем, какое из запомненых ранее подойдёт

inp = [int(x) for x in sys.stdin.read().strip().split()]
# inp = [15, 20, 33, 42, 15, 35, 16]
m = None
queue = []
without_max = None
with5_max = None
with3_max = None
with35_max = None

def max_with_None(a, b):
    if a == None and b == None:
        return None
    elif a == None:
        return b
    elif b == None:
        return a
    return max(a, b)

for i, n in enumerate(inp):
    heappush(queue, (i, n))
    if len(queue) > 5:
        _, something = heappop(queue)
        without_max = max_with_None(without_max, something)
        if something % 3 == 0:
            with3_max = max_with_None(with3_max, something)
        if something % 5 == 0:
            with5_max = max_with_None(with5_max, something)
        if something % 3 == 0 and something % 5 == 0:
            with35_max = max_with_None(with35_max, something)
    
    prev_maxes = [with35_max]
    if n % 3 == 0:
        prev_maxes.append(with5_max)
    if n % 5 == 0:
        prev_maxes.append(with3_max)
    if n % 3 == 0 and n % 5 == 0:
        prev_maxes.append(without_max)
    
    current_max = [x+n for x in prev_maxes if x != None]
    if len(current_max) == 0:
        current_max = None
    else:
        current_max = max(current_max)
    
    m = max_with_None(m, current_max)

print(m if m != None else 0)