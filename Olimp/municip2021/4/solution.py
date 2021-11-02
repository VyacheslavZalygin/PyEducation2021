n = int(input())
m = int(input())
a = [int(input()) for i in range(n)]
b = [int(input()) for i in range(m)]
times = sorted([-x for x in a] + b)
print(max(0, times[(n + m) // 2]))

