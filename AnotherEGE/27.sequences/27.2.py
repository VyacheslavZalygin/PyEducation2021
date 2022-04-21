with open('D:/repos/PyEducation2122/AnotherEGE/27.sequences/27-2b.txt') as f:
    _, *data = [int(x) for x in f.read().strip().split()] 

k = 7
counts = [0] * k

count = 0
for n in data:
    key = n % k
    alt_key = (k - key) % k
    count += counts[alt_key]
    counts[key] += 1

print(count)