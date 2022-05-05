import sys

def f(test):
    data = [int(x) for x in test.split()]

    if len(data) == 0:
        return 0

    prefix_sums = [0]
    for n in data: 
        prefix_sums.append(n + prefix_sums[-1])

    max_sum = max(prefix_sums[1:])
    min_sum = min(prefix_sums[:prefix_sums.index(max_sum)])
    return max_sum-min_sum

tests = (
        ('-3 2 3 -1 2 -10 5', 6),
        ('1 2 3 4 5 6 7', 28),
        ('', 0),
        ('-1 -2 -3 -4 -5 -6 -7 -8', -1),
        ('1 -10 -10 -10 4 56 1', 61),
        ('-10 1 2 3 -20 4 5 -15 15 -10 16', 15)
    )

for data, exp in tests:
    res = f(data)
    if res == exp:
        print('OK', res)
    else:
        print(f'exp: {exp}, act: {res}')