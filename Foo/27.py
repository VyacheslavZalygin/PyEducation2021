with open('27-B.txt') as f:
    data = [int(x) for x in f.read().strip().split()][1:]
div = 999

suffix_sum = [0]
for el in data:
    suffix_sum.append((suffix_sum[-1]+el) % div)
count = 0
table = {}
for s in suffix_sum:
    if s not in table:
        table[s] = 1
    else:
        count += table[s]
        table[s] += 1
print(count)