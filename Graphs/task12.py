def solve(graph):
    passed = []
    return get_max(graph, passed, 0)

def get_max(graph, passed, v):
    if v in passed:
        return None
    else:
        passed.append(v)
    e = get_edges(graph, v)
    if len(e) != 0:
        for n in e:
            m = get_max(graph, passed, n)
            if not m is None:
                return m
        return None
    else:
        return v

def get_edges(graph, v):
    return [] if v not in graph else [e for e in graph[v]]

# g = { 0: { 1: -1, 3: -1, 0: -1 },
#       1: { 3: -1, 2: -1},
#       2: { 1: -1 },
#       3: { 0: -1}}
# print(solve(g))
import sys
exec(sys.stdin.read())