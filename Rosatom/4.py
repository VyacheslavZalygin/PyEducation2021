import sys

def pow(a, b, n):
    if b == 0:
        return 1
    if b == 1:
        return a % n
    if not b % 2:
        return pow(((a%n) * (a%n))%n, b // 2, n)
    else:
        return ((a%n) * (pow(a, b-1, n)%n))%n

print(pow(13, 13**13, 100)%100)
print(6**(6**6) % 100)
print(pow(6, pow(6, 6, 100), 100))