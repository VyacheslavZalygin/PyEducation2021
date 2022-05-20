with open('D://repos/PyEducation2122/AnotherEGE/26/26-57.txt') as f:
    _, exp, *heap = [int(x) for x in f.read().strip().split()]

count = 0
heap = sorted(heap, reverse=True)
while sum(heap) >= exp:
    curr = heap.pop(0)
    while curr < exp:
        count += 1
        i = len(heap)-1
        while curr + heap[i] < exp and i > 0:
            i -= 1
        curr += heap.pop(i)
    if curr - exp > 0:
        heap.append(curr-exp)
    heap = sorted(heap, reverse=True)

print(count, len(heap))