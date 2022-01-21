import sys

n = sys.stdin.read()
n_prev = n[0]
for n_curr in n[1:]:
    if n_prev == n_curr:
        print("NO")
        exit()
    n_prev = n_curr
print("YES")