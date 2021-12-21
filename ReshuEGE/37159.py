with open('37159.txt') as f:
  s = f.read()

print(max([len(x) for x in s.replace('da', 'd a').replace('ad', 'a d').split(' ')]))