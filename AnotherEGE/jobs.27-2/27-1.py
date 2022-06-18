from itertools import accumulate


with open('D:\\repos\PyEducation2122\AnotherEGE\jobs.27-2\\27-1B.txt') as f:
    _, *a = [int(x) for x in f.read().split()]

a = a*2
l = len(a)//2
mid = sum(a)//4
с = 0
j = 1
mn_delta = float('inf')
mn_distance = float('inf')
s = a[0]
for i in range(l):
    while mid >= s:
        s += a[j]
        j += 1
    if abs(mid-s) > abs(mid-(s-a[j-1])):
        j -= 1
        s -= a[j]
    # print(a[i:j])
    if mn_delta > abs(mid-s):
        mn_delta = abs(mid-s)
        mn_distance = min(mn_distance, (j-1)-i, l-j+i-1)
    s -= a[i]
print(mn_distance)