def f(n):
    if n == 729:
        return [""]
    if n > 729:
        return ["NO WAY"]
    a = ["1"+x for x in f(n+1)]
    a.extend(["2"+x for x in f(n*2)])
    return a

print(f(17))