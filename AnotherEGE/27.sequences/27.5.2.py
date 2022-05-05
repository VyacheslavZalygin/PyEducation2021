# через рекурсию с мемоизацией

test = '-1 5 3 2 3 4 3 4 3' #5 4 5 5 5 1'
test1 = '5 1 2 2 3 5 4 5 5 5 1'
exp = 3

with open('D://repos/PyEducation2122/AnotherEGE/27.sequences/27-20a.txt') as f:
    _, *data = map(int, f.read().strip().split())
    data = [(data[i], data[i+1]) for i in range(0, len(data), 2)]
print(data)

def func(i, curr, last, max):
    if i == len(data):
        return curr
    a, b = data[i]

    maxes = [curr]
    if a == last or b == last:
        if a == last:
            maxes.append(func(i+1, curr+1, b))
        if b == last:
            maxes.append(func(i+1, 2, a))
    else:
        maxes.append(max(func(i+1, 1, b), func(i+1, 1, a)))
    return max(maxes)

# cache = {}
# memoized = func
# def func(i, curr, last):
#     if i not in cache:
#         cache = 

print(func(0, 1, -1))