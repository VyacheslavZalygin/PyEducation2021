from functools import lru_cache

def moves(h):
    return h+1, h+3, h*2

@lru_cache(None)
def game(h):
    if h >= 48:
        return 'end'
    if any(game(x)=='end' for x in moves(h)):
        return 'win1'
    if all(game(x)=='win1' for x in moves(h)):
        return 'lose1'
    if any(game(x)=='lose1' for x in moves(h)):
        return 'win2'
    if all(game(x)=='win1'or game(x)=='win2' for x in moves(h)):
        return 'lose2'
    return 'not stated'


for n in range(1, 48):
    print(n, game(n))