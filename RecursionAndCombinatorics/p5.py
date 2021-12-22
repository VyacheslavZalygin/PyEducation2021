#some research about p5

def f(n, k, m = 1):
    if n == 0 and k == 0: return 1
    res = 0
    for x in range(m, n+1):
        res += f(n-x, k-1, x)
    return res

def g(n, k):
    if k == 0: return [[]] if n == 0 else []
    return [
        [el+x for el in [0] + seq]
        for x in range(n+1)
        for seq in g(n-k*x, k-1)
    ]

def alt_f(n, k):
    return g(n-k, k)