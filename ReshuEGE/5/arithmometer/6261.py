def f(n):
    if n == 83:
        return [""]
    if n > 83:
        return ["NO WAY"]
    a = ["1"+x for x in f(n+1) if len(x) < 6]
    a.extend(["2"+x for x in f(n*4) if len(x) < 6])
    return a

print(f(4))