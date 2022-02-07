with open('17.txt') as f:
  arr = [int(x) for x in f.read().split()]

count = 0
m = 0
for i in range(len(arr)):
  for j in range(i+1, len(arr)):
    a, b = arr[i], arr[j]
    if abs(a-b) % 2 == 0 and (a % 31 == 0 or b % 31 == 0):
      count += 1
      if m < a+b:
        m = a+b
print(count, m)