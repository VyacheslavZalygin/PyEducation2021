# Определите максимальное количество идущих подряд символов, среди которых нет подстроки XZZY.

with open("36037.txt") as f:
  st = f.read()
  i = 0
  max_count = 0
  while i < len(st):
    a = st.find("XZZY", i)
    if a-i > max_count:
      max_count = a-i
    i += a
  print(max_count)
