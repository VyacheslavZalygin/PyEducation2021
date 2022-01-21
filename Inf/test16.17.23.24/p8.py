def func(a, b):
    if a == b: return 1
    if a > b: return 0
    if a == 33: return 0
    return func(a+1, b) + func(a*2, b) + func(a*3, b)

print(func(3, 15) * func(15, 50))