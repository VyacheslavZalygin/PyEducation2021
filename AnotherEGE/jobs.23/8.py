def f(a, c=0):
    if c == 7:  return {a}
    return f(a+1, c+1) | f(a+2, c+1) | f(a*2, c+1)

print(len(f(1)))
