import sys

s = sys.stdin.read().strip()
print(max([len(x) for x in s.replace('ad', 'a d').replace('da', 'd a').split(" ")]))