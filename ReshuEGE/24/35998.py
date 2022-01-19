def func(string):
  a = 0
  letters = {}
  m = -1
  for i, l in enumerate(string):
    if l == 'A':
      a += 1
    if not l in letters:
      letters[l] = i
    else:
      if m < i - letters[l]:
        m = i - letters[l]
  return m if a < 25 else -1

with open('35998.txt') as f:
  print(max([func(string) for string in f.read().split()]))