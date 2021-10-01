def solve(graph):
    return ways_count(graph, 0, 1)

def ways_count(graph, a, b):
    if a == b:
        return 1
    ns = neighbours(graph, a)
    if len(ns) != 0:
        return sum([ways_count(graph, n, b) for n in ns])
    return 0

def neighbours(graph, v):
    return [] if v not in graph else [e for e in graph[v]]

# g = { 0: { 2: -1, 3: -1},
#       2: { 1: -1, 3: -1},
#       3: { 1: -1} }
# print(solve(g))
import sys
exec(sys.stdin.read())