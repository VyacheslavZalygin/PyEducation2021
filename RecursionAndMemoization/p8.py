import sys

inp = [int(x) for x in sys.stdin.read().split()]
# вес, объём; объём = 100500
a = [inp[i:i+2] for i in range(0, len(inp), 2)]

def f(space):
    stack = [space]
    cache = {}
    while len(stack) != 0:
        free_space = stack[-1]
        res = []
        ready_to_compute = True
        required = []
        for (w, v) in a:
            if free_space-v > 0:
                if free_space-v in cache:
                    call = cache[free_space-v]
                    res.append(w+call if call != -1 else -1)
                else:
                    ready_to_compute = False
                    required.append(free_space-v)
            elif free_space-v == 0:
                res.append(w)
            else:
                res.append(-1)
        if ready_to_compute:
            stack.pop()
            if len(res) != 0:
                cache[free_space] = max(res)
            else:
                cache[free_space] = 0
        else:
            stack.extend(required)
    return cache[space]
    # b = []
    # for (w,v) in a:
    #     if space-v > 0:
    #         call = f(space-v)
    #         b.append(w+call if call != -1 else -1)
    #     elif space-v == 0:
    #         b.append(w)
    #     else:
    #         b.append(-1)
    # # print(space, b, max(b))
    # return max(b)

res = f(100500)
print(res if res != -1 else "NO")