with open('D:\\repos\PyEducation2122\AnotherEGE\jobs.24\\24-7.txt') as f:
    a = f.read()

def f(a):
    mx = 0
    c = 0
    for i in range(0, len(a), 3):
        if a[i:i+3] == 'XYZ' or a[i:i+3] == 'ZYX':
            c += 1
        else:
            mx = max(mx, c)
            c = 0
    mx = max(mx, c)
    return mx

print(f(a), f(a[1:]), f(a[2:]))