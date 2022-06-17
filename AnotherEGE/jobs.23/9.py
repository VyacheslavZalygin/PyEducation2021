def f(a, c=0):
    if c == 5:  return {a}
    return f(a+1, c+1) | f(a*2, c+1) | {a}
 
r = f(1)
c = 1
while c in r:
    c += 1
print(c)
