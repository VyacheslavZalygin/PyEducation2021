class Network:
  def __init__(self):
    self.node_array = []

  def node(self, children):
    self.node_array.append(children[:])
    return len(self.node_array)-1

  def values(self, nodes):
    result = [None for _ in range(len(self.node_array))]
    nodes = {n[0]: n[1] for n in nodes}
    for node in range(len(self.node_array)):
      if node in nodes:
        result[node] = nodes[node]
      else:
        result[node] = sum([result[n] for n in self.node_array[node]])
    return result

# foo = Network()
# node0 = foo.node([])
# node3 = foo.node([node0])
# node2 = foo.node([node0])
# node1 = foo.node([node0])
# node5 = foo.node([node2, node1])
# node4 = foo.node([node3, node5])
# print(foo.values([(0,1), (1, 5)]))

import sys
exec(sys.stdin.read())