import sys

inp = [int(x) for x in sys.stdin.read().split()]
# вес, объём; объём < 100500
a = [inp[i:i+2] for i in range(0, len(inp), 2)]

def f(space):
    stack = [space]
    cache = {}
    while len(stack) != 0:
        free_space = stack[-1]
        res = [0]
        ready_to_compute = True
        required = []
        for (w, v) in a:
            if free_space-v >= 0:
                if free_space-v in cache:
                    res.append(w+cache[free_space-v])
                else:
                    ready_to_compute = False
                    required.append(free_space-v)
        if ready_to_compute:
            stack.pop()
            cache[free_space] = max(res)
        else:
            stack.extend(required)
    return cache[space]
    # b = [(w+cache(free_space-v, f) if free_space-v >= 0 else 0) for (w, v) in a]
    # print(free_space, b, max(b))
    # return max(b)

print(f(100500))