def solve(graph):
  from heapq import heappush, heappop
  visited = {}
  queue = []
  heappush(queue, (0, 0, [0]))
  while len(queue) != 0 and 1 not in visited:
    length, vertex, way = heappop(queue)
    if vertex not in visited:
      visited[vertex] = way
      [heappush(queue, (length + graph[vertex][x], x, [*way, x])) for x in get_neighbours(graph, vertex) if x not in visited]
  return visited[1] if 1 in visited else None

def get_neighbours(graph, vertex):
  return [] if vertex not in graph else [e for e in graph[vertex]]

# g = {0: {2: 2, 3: 1},
#      2: {3: 1, 1: 2},
#      3: {1: 1}}
# g = { 1: { 3: 0},
#       3: { 1: 0}}
# print(solve(g))
import sys
exec(sys.stdin.read())