start_week = 1633305600
delta = 604800 # длина недели
data = [0 for _ in range(delta)]

with open('26.txt') as f:
  s = f.read().split()[1:]

arr = [(int(s[i]), int(s[i])) for i in range(0, len(s), 2)]
arr.sort()
nulls = arr.count((0, 0))
for j, (start, end) in enumerate(arr[nulls:]):
  if j % 10 == 0: print(j, (start, end))
  if start > start_week + delta:
    continue
  if start != 0:
    if start > start_week:
      start -= start_week
    else:
      start = 0
  if end == 0:
    end = delta
  for i in range(start, min(end+1, delta)):
    # print(i)
    data[i] += 1

print(max(data))
print(nulls)