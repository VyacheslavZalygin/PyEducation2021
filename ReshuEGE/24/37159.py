# Текстовый файл состоит из строчных букв английского алфавита. Найдите максимальную длину подстроки, в которой символы «a» и «d» не стоят рядом.

with open("37159.txt") as f:
  st = f.read()
  max_c = 0
  c = 1
  for i in range(1, len(st)):
    if st[i] == "a" and st[i-1] == "d" or \
       st[i] == "d" and st[i-1] == "a":
      if max_c < c:
        max_c = c
      c = 1
    else:
      c += 1
  print(max_c)
