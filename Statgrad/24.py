with open('22.txt') as f:
  data = f.read().strip()
  data = data[data.index('A'):len(data)-data[::-1].index('A')]
  data = [x for x in data.split('A')  if len(x) >= 10 and x.count('B') >= 2]
  print(len(data))