def f(n):
    n = bin(n)[2:]
    for _ in range(3):
        one, null = 0, 0
        for x in n:
            if x == "1": one += 1
            else: null += 1
        if one == null:
            n += n[-1]
        else:
            if one < null:
                n += "1"
            else:
                n += "0"
    return int(n, 2)

for n in range(105, 1000):
    if f(n) % 4 == 0:
        print(n)
        break