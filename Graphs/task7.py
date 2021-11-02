def solve(graph):
    table = {}
    top_sort(graph, table, 0)
    m = max(table.values())
    for vertex in table:
        table[vertex] = m - table[vertex]
    # print(normalize(table))
    return table

def top_sort(graph, table, vertex):
    if not vertex in table:
        p = [top_sort(graph, table, x) for x in get_neighbours(graph, vertex)]
        if len(p) != 0:
            table[vertex] = 1 + max(p)
        else:
            table[vertex] = 0
    return table[vertex]

def get_neighbours(graph, vertex):
    return [] if vertex not in graph else [e for e in graph[vertex]]

def normalize(table):
    t = []
    for vertex in table:
        t.append((vertex, table[vertex]))
    l = len(t)
    for _ in range(l):
        for i in range(l - 1):
            if t[i][1] > t[i + 1][1]:
                t[i], t[i + 1] = t[i + 1], t[i]
    t = [pair[0] for pair in t]
    return t

# g = { 0: { 5: 4, 3: 3, 4:1 },
#       2: { 1: 3 },
#       3: { 2: 3, 5: 4 },
#       5: { 2: 3 } }
# g = {
#     0: { 1: 0, 2: 0},
#     2: { 1: 0, 4: 0},
#     3: { 1: 0},
# }
# print(solve(g))
import sys
exec(sys.stdin.read())