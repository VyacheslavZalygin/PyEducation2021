import math
import sys

class Arr:
    def __init__(self, a: int, b: int):
        self.arr = [True for _ in range(b-a)]
        self.a = a
        self.b = b

    def __getitem__(self, i: int):
        if not self.validate(i):
            raise IndexError('I is not between a and b. i: ' + str(i) + ', a-b: ' + str(self.a) + '-' + str(self.b))
        return self.arr[int(i)-self.a]

    def validate(self, i: int):
        if int(i) >= self.a and i < self.b:
            return True
        return False

    def __setitem__(self, i: int, value: bool):
        if not self.validate(i):
            raise IndexError('I is not between a and b. i: ' + str(i) + ', a-b: ' + str(self.a) + '-' + str(self.b))
        self.arr[int(i)-self.a] = value

def main():
    a, b = [int(x) for x in sys.stdin.read().split()]
    block = Arr(a, b)
    seq = Arr(2, int(math.sqrt(b)+2))

    prime = 2
    while seq.validate(prime):
        cur = a - a % prime
        if a % prime != 0 or a == 0:
            cur += prime
        while block.validate(cur):
            block[cur] = False
            cur += prime

        cur = prime*2
        while seq.validate(cur):
            seq[cur] = False
            cur += prime
        cur = prime+1

        while seq.validate(cur):
            if seq[cur]: break
            cur += 1
        prime = cur

    for i in range(block.a, block.b):
        if block[i]:
            print(i, end=' ')

main()