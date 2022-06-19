with open('D:\\repos\PyEducation2122\AnotherEGE\jobs.24\\24-2.txt') as f:
    a = f.read()

print(max(map(len, a.replace('PR', 'P R').replace('RP', 'R P').split())))