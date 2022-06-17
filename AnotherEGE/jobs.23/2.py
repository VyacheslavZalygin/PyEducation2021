def f(a, b, t = False):
    if a == b: return 1
    if a > b: return 0
    return (f(a*2, b, True) + f(a*3, b, True) if not t else 0) + f(a+1, b)

print(f(1, 30))