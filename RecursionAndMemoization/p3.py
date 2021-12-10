from math import log2
import sys

n, k = [int(x) for x in sys.stdin.read().split()]
l = int(log2(k))+1
print(l if n > l else n)