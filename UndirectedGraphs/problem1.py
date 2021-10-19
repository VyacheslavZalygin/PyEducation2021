def solve(graph):
  visited = {}
  stack = [0]
  while len(stack) != 0:
    vertex = stack.pop()
    visited[vertex] = 0
    stack.extend([x for x in get_neighbours(graph, vertex) if not x in visited])
  return list(visited.keys())

def get_neighbours(graph, v):
  return [] if v not in graph else [e for e in graph[v]]

# g = {0: {1: 0, 2: 0},
#      1: {0: 0, 2: 0, 4: 0},
#      2: {0: 0, 1: 0},
#      4: {1: 0},
#      5: {6: 0}, 6: {5: 0}}
# g = { 1: { 3: 0},
#       3: { 1: 0}}
# print(solve(g))
import sys
exec(sys.stdin.read())