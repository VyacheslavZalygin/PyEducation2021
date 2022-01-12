def func(s):
  a_count = 0
  for c in s:
    if c == "A": a_count += 1
    if a_count == 3:
      break
  else:
    return 0
  return len(s)

with open("40999.txt") as f:
  print(max([func(x) for x in f.read().split("E")])) # 275