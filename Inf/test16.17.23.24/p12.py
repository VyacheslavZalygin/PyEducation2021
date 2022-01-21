import sys

def process(line):
    table = {}
    count = 0
    for letter in line:
        if letter == "N": count += 1
        if letter not in table:
            table[letter] = 1
        else:
            table[letter] += 1
    if count != 0:
        return (count, max(table.items(), key=lambda p: (p[1], p[0]))[0])
    else:
        return None

a = [process(x) for x in sys.stdin.read().split() if process(x) != None]
if len(a) != 0:
    print(min(a, key=lambda p: p[0])[1])
else:
    print(None)