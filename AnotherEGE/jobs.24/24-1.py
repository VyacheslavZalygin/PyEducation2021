with open('D:\\repos\PyEducation2122\AnotherEGE\jobs.24\\24-1.txt') as f:
    a = f.read()

print(max(map(len, a.replace('W', ' ').replace('R', ' ').replace('Q', ' ').split())))