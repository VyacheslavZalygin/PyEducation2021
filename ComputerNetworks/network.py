class Network:
  def __init__(self):
    self.node_array = []

  def node(self, combine, children):
    self.node_array.append((combine, children[:]))
    return len(self.node_array)-1

  def values(self, nodes):
    result = [None for _ in range(len(self.node_array))]
    nodes = {n[0]: n[1] for n in nodes}
    for node_id in range(len(self.node_array)):
      if node_id in nodes:
        result[node_id] = nodes[node_id]
      else:
        node = self.get_node(node_id)
        result[node_id] = node[0]([result[n] for n in node[1]])
    return result

  def get_node(self, node_id):
    return self.node_array[node_id]

# foo = Network()
# node0 = foo.node(sum, [])
# node3 = foo.node(sum, [node0])
# node2 = foo.node(sum, [node0])
# node1 = foo.node(sum, [node0])
# node5 = foo.node(sum, [node2, node1])
# node4 = foo.node(sum, [node3, node5])
# print(foo.values([(0,1), (1, 5)]))

import sys
exec(sys.stdin.read())