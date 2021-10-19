# heap queue test
from heapq import heappop, heappush
queue = []
heappush(queue, (2, [2, 4, 1]))
heappush(queue, (1, []))
print(heappop(queue))
