# В строках, содержащих менее 25 букв G, нужно определить и вывести максимальное расстояние между одинаковыми буквами в одной строке.
def func(st):
  g_count = 0
  table = {}
  max_l = 1
  for i, c in enumerate(st):
    if c == "G":
      g_count += 1
    if c not in table:
      table[c] = i
    else:
      if i - table[c] > max_l:
        max_l = i - table[c]
  return max_l if g_count < 25 else 0

with open("36879.txt") as f:
  print(max([func(x) for x in f.read().split()])) # 1001
  