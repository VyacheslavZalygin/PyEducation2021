def get_network(ip, mask):
    return tuple(ip_oct & mask_oct \
                    for ip_oct, mask_oct in zip(ip, mask))

with open('d:/repos/PyEducation2122/AnotherEGE/26/26-2.txt') as f:
    _, *octs = [int(x) for x in f.read().split()]

mask = (255, 255, 224, 0)
ips = [(octs[i], octs[i+1], octs[i+2], octs[i+3]) \
            for i in range(0, len(octs), 4)]

ntws = {}
for ip in ips:
    ntw = get_network(ip, mask)
    if ntw not in ntws:
        ntws[ntw] = (1, set())
    else:
        count, ips = ntws[ntw]
        ntws[ntw] = (count+1, ips | {ip})

ntws = sorted([(x, ntws[x]) for x in ntws], \
                key=lambda y: (-y[1][0], y[0]))

tmp = list(map(lambda x: (x[0], x[1][0], len(x[1][1])), ntws))[:10]
for x in tmp:
    print(x)
# print('.'.join(map(str, ntw[0])), len(ntw[1][1]))