# +1, +2, *2
def f(a, b, c=0):
    if a == b:  return 1
    if a > b:   return 0
    else:       return (f(a*2, b, c+1) if c < 2 else 0) + f(a+1, b, c) + f(a+2, b, c)

print(f(2, 12))