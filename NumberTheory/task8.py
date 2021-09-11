import sys

class Arr:
    def __init__(self, a, b):
        self.arr = [True for _ in range(a-b)]
        self.a = a
        self.b = b

    def __getitem__(self, item):
        return self.arr[int(item)-self.a]

def main():
    a, b = [int(x) for x in sys.stdin.read().split()]
    arr = Arr(a, b)
    print(arr[6])

main()