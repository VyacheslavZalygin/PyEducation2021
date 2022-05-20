# m = 6
# 2, 3

# m = 30
# 2, 3, 5, 6, 15, 10

# 2 3 5: 30
# 2 3 4: 12
# 2 3 4 5: 

from itertools import product

alph = [2, 3, 5, 7, 11, 13]

l = 0
for i in range(1, len(alph)):
    tmp = set(tuple(sorted(x)) for x in product(alph, repeat=i))
        # for x in product(alph, repeat=i) 
        # if len(x) == 1 or all(a != b for a, b in zip(x, x[1:]))
        # )
    print(tmp)
    l += len(tmp)
print(l)