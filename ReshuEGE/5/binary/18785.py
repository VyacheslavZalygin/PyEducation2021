def f(n):
    n = bin(n)[2:]
    if int(n) % 2 == 0:
        n = "1" + n + "0"
    else:
        n = "11" + n + "11"
    return int(n, 2)

for n in range(1, 100):
    if f(n) > 52:
        print(n)
        break

print(3, f(2))