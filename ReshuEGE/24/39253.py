# Определите максимальное количество идущих подряд символов, среди которых не более одной буквы D.
# 354

with open("39253.txt") as f:
  a = [len(x) for x in f.read().split("D")]
  b = [a[i]+a[i+1]+1 for i in range(len(a)-2)]
  print(max(a), max(b))