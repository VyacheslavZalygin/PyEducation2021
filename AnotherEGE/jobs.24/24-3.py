with open('D:\\repos\PyEducation2122\AnotherEGE\jobs.24\\24-3.txt') as f:
    a = f.read()

print(max(map(len, a.replace('PP', 'P P').split())))