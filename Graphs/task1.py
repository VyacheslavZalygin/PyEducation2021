def solve(graph):
    m_v = -1
    for key, value in graph[0].pair():
        if key >= m_v and ((key in graph and len(graph[key]) == 0) or (key not in graph)):
            m_v = key
    if m_v != -1:
        return m_v
    return

g = { 0: { 1: -1, 3: -1, 7: -1},
      1: { 4: -1, 3: -1},
      3: { }}
print(solve(g))
import sys
exec(sys.stdin.read())