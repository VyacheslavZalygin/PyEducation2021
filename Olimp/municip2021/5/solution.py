import sys

n = int(input())
a = [int(input()) for i in range(n)]


# Case: + - +
sum_prefix = 0
i = 0
while i < n and sum_prefix <= 0:
    sum_prefix += a[i]
    i += 1

sum_suffix = 0
j = n - 1
while j >= 0 and sum_suffix <= 0:
    sum_suffix += a[j]
    j -= 1

if i <= j:
    print(i, j + 1 - i, n - j - 1)
    sys.exit(0)

# Case: + + -
sum_prefix = 0
best_sum_prefix = 10 ** 9 + 1
best_prev_i = 0
i = 0
while i < len(a) - 1:
    sum_prefix += a[i]
    if sum_prefix - best_sum_prefix > 0:
        print(best_prev_i + 1, i - best_prev_i, n - 1 - i)
        sys.exit(0)
    if best_sum_prefix > sum_prefix > 0:
        best_sum_prefix = sum_prefix
        best_prev_i = i
    i += 1

# Case: - + +
sum_suffix = 0
best_sum_suffix = 10 ** 9 + 1
best_prev_i = n - 1
i = n - 1
while i > 0:
    sum_suffix += a[i]
    if sum_suffix - best_sum_suffix > 0:
        print(i, best_prev_i - i, n - best_prev_i)
        sys.exit(0)
    if best_sum_suffix > sum_suffix > 0:
        best_sum_suffix = sum_suffix
        best_prev_i = i
    i -= 1

print(0)
    
