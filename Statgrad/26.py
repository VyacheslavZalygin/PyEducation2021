with open('26.txt') as f:
  _, *data =[[int(y) for y in x.split()] for x in f.read().strip().split('\n')[1:]]
  table, data = {}, set([(a, b) for a, b in data if b % 2 == 1])
  data = sorted(data, key=lambda pair: pair[1])
  for a, b in data:
    if a not in table: table[a] = [b]
    else:              table[a].append(b)
  data = [(x, table[x]) for x in sorted(table)]
  a, b = max(data, key=lambda pair: len(pair[1])) 
  print(len(b), a)