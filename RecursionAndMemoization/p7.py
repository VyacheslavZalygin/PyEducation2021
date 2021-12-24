import sys

class Item:
    def __init__(self, weight, volume):
        self.weight = weight
        self.volume = volume
        self.koef = weight/volume

def max_weight(items, free_volume):
    i = 0
    res = 0
    while free_volume > 0:
        while i < len(items):
            m = items[i]
            if m.volume <= free_volume:
                break
            i += 1
        else:
            return None
        n = (free_volume // m.volume)
        res += m.weight*n
        free_volume -= m.volume*n
    return res

a = [int(x) for x in sys.stdin.read().split()]
item_arr = [Item(a[i], a[i+1]) for i in range(0, len(a), 2)]
item_arr = sorted(item_arr, key=lambda i: i.koef, reverse=True)
print(max_weight(item_arr, 100500))