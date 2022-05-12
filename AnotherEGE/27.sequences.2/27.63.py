with open('D://repos/PyEducation2122/AnotherEGE/27.sequences.2/27-63b.txt') as f:
    _, *data = [int(x) for x in f.read().strip().split()]

K = 9
arr = [[] for _ in range(K)]

data = sorted(data)
print(data)

# for n in data:
#     arr[n%K].append(n)

s = sum(data[:4])
if s % 9 == 0:
    for n in data[4:]:
        if (s - data[3] + n) % 9 != 0:
            print(s-data[3]+n)
            print(n)
            break
else:
    print(s)

# print(arr)
# print(data[:4])
# print(sum(data[:4]))