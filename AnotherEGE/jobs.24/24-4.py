with open('D:\\repos\PyEducation2122\AnotherEGE\jobs.24\\24-4.txt') as f:
    a = f.read()

print(max(map(len, a.replace('XVIII', 'XVII VIII').split())))