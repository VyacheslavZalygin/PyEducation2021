def solve(graph):
  skeleton = {}
  stack = [0]
  visited = {}
  while len(stack) != 0:
    vertex = stack.pop()
    if vertex not in skeleton:
      skeleton[vertex] = {}
    for neighbour in get_neighbours(graph, vertex):
      if neighbour not in skeleton and neighbour not in visited:
        skeleton[vertex][neighbour] = 0
        visited[neighbour] = 0
        stack.append(neighbour)
  return skeleton

def get_neighbours(graph, v):
  return [] if v not in graph else [e for e in graph[v]]

# g = {0: {1: 0, 2: 0},
#      1: {0: 0, 2: 0, 4: 0},
#      2: {0: 0, 1: 0},
#      4: {1: 0, 0: 0},
#      5: {6: 0}, 6: {5: 0}}
# g = { 1: { 3: 0},
#       3: { 1: 0}}
# print(solve(g))
import sys
exec(sys.stdin.read())