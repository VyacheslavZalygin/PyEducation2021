def solve(graph):
    table = ()
    way, l = min_way(graph, table, 0, 1)
    way.reverse()
    return way, l

def min_way(graph, table, a, b):
    if a == b:
        return [a], 0
    if a not in table:
        ns = neighbours(graph, a)
        if len(ns) != 0:
            m_w, l = [], None
            for n in ns:
                way, length = min_way(graph, table, n, b)
                if len(way) != 0 and (l is None or length + graph[a][way[-1]] < l):
                    m_w, l = way, length + graph[a][way[-1]]
            if not l is None:
                m_w.append(a)
            table.append(a)
            return m_w, l
    return [], None

def add_v(table, v):
    pass

def neighbours(graph, v):
    return [] if v not in graph else [e for e in graph[v]]

g = { 0: { 5:1, 3:3, 4:1, 0: 1 },
      2: { 1:3 },
      3: { 2:4, 5:5 },
      5: { 2:6} }
print(solve(g))
# import sys
# exec(sys.stdin.read())