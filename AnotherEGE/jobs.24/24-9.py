with open('D:\\repos\PyEducation2122\AnotherEGE\jobs.24\\24-9.txt') as f:
    a = f.read()
# a = 'BDEABCBABCABBD'
# a = a.replace('ABC', '*C').replace('BAC', '*C').replace('CAB', '*B').replace('CBA', '*A')

mx = 0
c = 0
i = 0
while i < len(a)-3:
    if a[i:i+3] in {'ABC', 'BAC', 'CAB', 'CBA'}:
        c += 1
        i += 2
    else:
        mx = max(mx, c)
        c = 0
        i += 1
mx = max(mx, c)
print(mx)