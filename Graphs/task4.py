def solve(graph):
    ws = ways(graph, 0, 1)
    for w in ws: w.reverse()
    return ws

def ways2(graph, a, b):
    if a == b:
        return [[a]]
    ns = neighbours(graph, a)
    if len(ns) != 0:
        ws = []
        for n in ns:
            ws_p = ways2(graph, n, b)
            if not ws_p is None:
                ws.extend(ws_p)
        for w in ws:
            w.append(a)
        return ws
    else:
        return None

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

# g = { 0: {5:0,3:0}, 2:{1:0}, 3:{2:0, 5:0}, 5:{2:0} }
# print(solve(g))
import sys
exec(sys.stdin.read())