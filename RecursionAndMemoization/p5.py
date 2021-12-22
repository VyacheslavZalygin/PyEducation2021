FIRST = 1
SECOND = -1
c = {}

def cache(args, func):
    if args not in c:
        c[args] = func(*args) 
    return c[args]

def is_first_player_win(a, b, p=FIRST):
    if a <= 0 or b <= 0:
        return p == SECOND # второй игрок уже не может сделать ход
    next = [(a-1, b), (a-2, b), (a-3, b),
            (a, b-1), (a, b-2), (a, b-3) ]
    if a % 2 == 0: next.append((a//2, b))
    if b % 2 == 0: next.append((a, b//2))
    next = [cache((*data, -p), is_first_player_win) for data in next]
    return True in next if p == FIRST else False not in next

import sys
n = int(sys.stdin.read())
res = 0
for i in range(1, n):
    # print(i, n-i)
    # print(is_first_player_win(i, n-i))
    res += int(is_first_player_win(i, n-i))
print(res)