# +1, +2, *2
def f(a, b, c=False):
    if a == b:              return 1
    if a % 2 == 1 and c:    return 0
    if a > b:               return 0
    else:                   return f(a+1, b, c or a%2==1) + f(a+2, b, c or a%2==1) + f(a*2, b, c or a%2==1)

print(f(2, 40))