with open('D:\\repos\PyEducation2122\AnotherEGE\jobs.24\\24-5.txt') as f:
    a = f.read()

print(max(map(len, a.replace('ZX', '*').replace('ZY', '*').replace('X', ' ').replace('Y', ' ').replace('Z', ' ').split())))