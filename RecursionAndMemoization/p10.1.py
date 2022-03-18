import sys

text = sys.stdin.read().strip()

table = {}
def project(k, x):
    if (k, x) in table: return table[(k, x)]

    if k == 1: answer = text[x:x+1]
    else: answer = (project(k//2, x), project(k//2, x+k//2))

    table[(k, x)] = answer
    return answer

N = 1
while N < len(text): N *= 2
print(*sorted(range(len(text)+1), key=lambda x: project(N, x)))