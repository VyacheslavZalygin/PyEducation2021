def solve(graph):
  from queue import Queue
  visited = {}
  queue = Queue()
  queue.put((0, 0, [0]))
  while not queue.empty() and 1 not in visited:
    vertex, length, way = queue.get()
    if vertex not in visited:
      visited[vertex] = way
      [queue.put((x, length + 1, [*way, x])) for x in get_neighbours(graph, vertex) if x not in visited]
  return visited[1] if 1 in visited else None

def get_neighbours(graph, vertex):
  return [] if vertex not in graph else [e for e in graph[vertex]]

# g = {0: {2: 2, 3: 5},
#      2: {3: 1, 1: 3},
#      3: {1: 1}}
# g = { 1: { 3: 0},
#       3: { 1: 0}}
# print(solve(g))
import sys
exec(sys.stdin.read())