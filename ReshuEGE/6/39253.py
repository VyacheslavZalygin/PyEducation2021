def f(s):
    s = 3 * (s // 10)
    n = 1
    while s < 221:
        s = s + 13
        n = n * 2
    return n

count = 0
for s in range(10, 1000):
    if f(s) == 256:
        count += 1
        print(s)

print(count)