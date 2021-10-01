def solve(graph):
    ws = ways(graph, 0, 1)
    for w in ws: w.reverse()
    max_length = None
    max_way = None
    for w in ws:
        curr_length = 0
        for i in range(len(w)-1):
            a, b = w[i], w[i+1]
            curr_length += graph[a][b]
        if max_length is None or max_length < curr_length:
            max_length = curr_length
            max_way = w
    return max_way

def ways(graph, a, b):
    if a == b:
        return [[a]]
    ns = neighbours(graph, a)
    if len(ns) != 0:
        ws = []
        for n in ns:
            ws_p = ways(graph, n, b)
            ws.extend(ws_p)
        for w in ws:
            w.append(a)
        return ws
    else:
        return []

def neighbours(graph, v):
    return [] if v not in graph else [e for e in graph[v]]

# g = { 0: {5:1,3:2}, 2:{1:3}, 3:{2:4, 5:5}, 5:{2:6} }
# print(solve(g))
import sys
exec(sys.stdin.read())