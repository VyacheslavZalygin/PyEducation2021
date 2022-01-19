import sys

def process(line):
    table = {}
    max_len = 0
    count = 0
    for i, letter in enumerate(line):
        if letter == "A":
            count += 1
        if letter not in table:
            table[letter] = i
        else:
            if max_len < i - table[letter]:
                max_len = i - table[letter]
    return max_len if count < 25 else -1

a = max([process(x) for x in sys.stdin.read().split()])
print(a if a != -1 else None)
