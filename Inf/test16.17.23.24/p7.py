ext = 0

def func(a, b):
    if a == b: return 1
    if a > b: return 0
    # if ext == a: return 0
    return func(a+1, b) + func(a+2, b) + func(a*3, b)

print(func(2, 8) * func(8, 10) * func(10, 12))