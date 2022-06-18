from itertools import accumulate
# A: 
# B: 
with open('D:\\repos\PyEducation2122\AnotherEGE\jobs.27-2\\27-4A.txt') as f:
    _, __, *a = [int(x) for x in f.read().split()]

a = a+a
pref = list(accumulate(a))

