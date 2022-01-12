# Определите максимальное количество идущих подряд символов в прилагаемом файле, среди которых нет идущих подряд символов P.

with open("38602.txt") as f:
  st = f.read()
  max_count = 0
  count = 0
  for i in range(1, len(st)):
    if st[i] == "P":
      if st[i] != st[i-1]:
        count += 1
      else:
        if count > max_count:
          max_count = count
        count = 1
    else:
      count += 1
  print(max_count) # 188