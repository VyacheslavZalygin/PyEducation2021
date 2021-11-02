T = input()
S = input()
n = int(input())

Sn = ""
while len(Sn) < len(T) + len(S):
    Sn += S

ans = 0
for i in range(len(S)):
    if Sn[i:i + len(T)] == T:
        k = (i + len(T) + len(S) - 1) // len(S)
        ans += max(n + 1 - k, 0)

print(ans)

