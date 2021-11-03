import sys

# n - количетсво мест на первом ряду, k - номер места
n, k = [int(x) for x in sys.stdin.read().split()]
s = (k // (2*n+1))*2
k %= (2*n+1)
if k > n:
  s += 1
  k -= n
elif k == 0:
  s -= 1
  k += n + s%2
print(s+1, k)
