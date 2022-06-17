def euclidian(x, y):
    while x != 0:
        x, y = y%x, x
    return y

count = 0
for x in range(1019, 100_000+1, 1019):
    for y in range(1019, 100_000+1, 1019):
        if euclidian(x, y) == 1019:
            count += 1
print(count)