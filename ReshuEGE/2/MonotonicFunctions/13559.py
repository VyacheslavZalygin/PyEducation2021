# yxz

for x in range(2):
    for y in range(2):
        for z in range(2):
            if ((not y) and (x or (not z))) == True:
                print(x, y, z)