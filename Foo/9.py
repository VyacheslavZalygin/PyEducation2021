with open('09.csv') as f:
    data = [[int(x) for x in row.strip().split(';')] for row in f.read().strip().split('\n')]