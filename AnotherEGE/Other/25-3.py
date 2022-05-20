def d(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

for n in range(17, 20+1):
    n = 2**n
    
    for j in range(n-5, n+6):
        if j == n: continue

        if 99999 <= j <= 1048571 and d(j):
            print(j, n)