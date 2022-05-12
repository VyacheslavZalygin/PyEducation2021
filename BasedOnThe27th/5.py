import sys

def f(input):
    data = [int(x) for x in input.split()]

    if len(data) == 0:
        return 0

    last_m = None
    last = None
    m = None
    for e in data:
        if last == None:
            last_m = e
            m = last_m
            last = e
            continue
        
        last_m = max((last_m+e, last+e, e))
        m = max(m, last_m)
        last = e

    return max(m, 0)

# tests = (
#         ('-3 2 3 -1 2 -10 5', 6),
#         ('1 2 3 4 5 6 7', 28),
#         ('', 0),
#         ('-1 -2 -3 -4 -5 -6 -7 -8', 0),
#         ('1 -10 -10 -10 4 56 1', 61),
#         ('-10 1 2 3 -20 4 5 -15 15 -10 16', 21)
#     )

# for data, exp in tests:
#     res = f(data)
#     if res == exp:
#         print('OK', res)
#     else:
#         print(f'exp: {exp}, act: {res}')

print(f(sys.stdin.read()))