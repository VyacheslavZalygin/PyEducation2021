import sys

data = [[int(x) for x in string.split()] for string in sys.stdin.read().split("\n") if string != ""]