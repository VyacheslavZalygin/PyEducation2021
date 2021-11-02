x = int(input())
y = int(input())

if (x + y) % 2 == 1:
    print(-1)
elif x == y > 0:
    print(0)
elif -x < y < x:
    print(1)
    print((x + y) // 2, (x + y) // 2, 'H')
elif y > -x:
    print(1)
    print((x + y) // 2, (x + y) // 2, 'V')
elif x > y:
    print(2)
    print(1, 1, 'H')
    print(1 + (x - y) // 2, 1 - (x - y) // 2, 'V')
elif x < y:
    print(2)
    print(1, 1, 'V')
    print(1 - (y - x) // 2, 1 + (y - x) // 2, 'H')
else:
    print(3)
    print(1, 1, 'H')
    print(2, 0, 'V')
    print(x + 1, y - 1, 'H')

