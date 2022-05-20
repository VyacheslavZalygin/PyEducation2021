import sys

DIV = 5

def f(input):
    data = [int(x) for x in input.split()]

    if len(data) == 0:
        return 0

    rems = [[None, None] for _ in range(DIV)]
    last_m = None
    count = 0
    for e in data:
        if last_m == None:
            last_m = e
        else:
            last_m += e

        count += e % 2
        key = count % DIV
        if rems[key][0] == None or rems[key][0] > last_m: 
            rems[key][0] = last_m
        elif rems[key][1] == None or rems[key][1] < last_m: 
            rems[key][1] = last_m

    return rems

tests = (
        ('-3 2 3 -1 2 -10 5', 0),
        ('1 2 3 4 5 6 7', 0),
        ('', 0),
        ('-1 -2 -3 -4 -5 -6 -7 -8', 0),
        ('1 -10 -10 -10 4 56 1', 0),
        ('-10 1 2 3 -20 4 5 -15 15 -10 16', 16),
        ('-10 1 2 3 -20 4 5 -15 15 -10 16 19', 19)
    )

for data, exp in tests:
    res = f(data)
    if res == exp:
        print('OK', exp, res)
    else:
        print(f'exp: {exp}, act: {res}')

# print(f(sys.stdin.read()))