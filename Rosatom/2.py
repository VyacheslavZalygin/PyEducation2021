for a in range(1, 1000):
  for b in range(1, 1000):
    if (4*a-3) % b == 0 and (4*b-1) % a == 0:
      print(a, b)