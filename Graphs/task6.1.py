def solve(graph):
    visited = []
    min_ways = {}
    way, l = get_min_way(graph, visited, min_ways, 0, 1)
    way.reverse()
    if l is None:
        return None
    return way

def get_min_way(graph, visited, min_ways, a, b):
    visited.append(a)
    if a == b:
        return [a], 0
    neighbours = get_neighbours(graph, a)
    min_way, min_length = [], None
    for n in neighbours:
        if not n in visited:
            if not n in min_ways:
                way, length = get_min_way(graph, visited[:], min_ways, n, b)
            else:
                way, length = min_ways[n]

            if not length is None:
                if min_length is None or length + graph[a][n] < min_length:
                    min_way, min_length = way, length + graph[a][n]
    if not min_length is None:
        min_way.append(a)
        min_ways[a] = (min_way[:], min_length)
    return min_way, min_length

def get_neighbours(graph, v):
    return [] if v not in graph else [e for e in graph[v]]

# g = { 0: { 5: 4, 3: 3, 4:1, 0: 1 },
#       2: { 1: 3, 3: 2},
#       1: { 10: -1, 2: 0 },
#       3: { 2: 3, 5: 4 },
#       5: { 2: 3 } }
# print(solve(g))
import sys
exec(sys.stdin.read())
