def f(a, b):
    if a == b:  return {a}
    if a > b:   return set()
    else:       return f(a*3, b) | f(a+3, b) | {a}

print(len([x for x in f(1, 100) if x % 2 == 1]))
