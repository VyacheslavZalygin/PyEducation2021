start_week = 1633305600
delta = 604800 # длина недели
data = [0 for _ in range(delta)]

with open('26.txt') as f:
  s = f.read().split()[1:]

arr = [(int(s[i]), int(s[i])) for i in range(0, len(s), 2)]
arr.sort()
nulls = arr.count((0, 0))
table = {}
for j, (start, end) in enumerate(arr[nulls:]):
  # if j % 10 == 0: print(j, (start, end))
  if start > start_week + delta:
    continue
  if start != 0:
    if start > start_week:
      start -= start_week
    else:
      start = 0
  if end == 0:
    end = delta
  if start not in table: table[start] = 0
  if end not in table: table[end] = 0
  table[start] += 1
  table[end] -= 1
print('next')

keys = list(table.keys())
keys.sort()
curr = nulls
m = 0
secs = 0
for key in keys:
  curr += table[key]
  m = max(curr, m)

curr = nulls
for key in keys:
  curr += table[key]
  if curr == m:
    secs += 1

print(m, secs)
# 12586
# 8587