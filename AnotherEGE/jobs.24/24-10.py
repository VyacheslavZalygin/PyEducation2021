with open('D:\\repos\PyEducation2122\AnotherEGE\jobs.24\\24-10.txt') as f:
    a = f.read()
# a = 'ZXYZXYYZZXZZXYXYZZXY'
a = a.replace('ZZXY', '*** **').replace('XY', '**').replace('ZZX', '***')
print(a)
a = a.replace('X', ' ').replace('Y', ' ').replace('Z', ' ')
print(a)
print(max(map(len, a.split())))