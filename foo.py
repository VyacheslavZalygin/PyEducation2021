print("l k b a")
for l in range(1, 20):
  for k in range(1, 20):
    if l*k != 16:
      b = (1+3*l)/(16-l*k)
      if b > 0 and b.is_integer():
        a = (b*k+3)/4
        print(l, k, int(b), a)