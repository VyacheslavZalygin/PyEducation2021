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
        result[node_id] = node[0][0]([result[n] for n in node[1]])
    return result

  def get_node(self, node_id):
    return self.node_array[node_id]

  def derivatives(self, values, node_id):
    result = [0 for _ in range(len(self.node_array))]
    result[node_id] = 1
    stack = [node_id]
    while len(stack) != 0:
      parent_id = stack.pop()
      parent = self.get_node(parent_id)
      if parent[0] == None: continue
      v = parent[0][1]([values[cid] for cid in parent[1]])
      for i, child_id in enumerate(parent[1]):
        result[child_id] += result[parent_id] * v[i]
        stack.append(child_id)
    return result

# def sum_gradient(inputs):
#   return [1 for _ in inputs]
#
# def product(inputs):
#   result = 1
#   for x in inputs: result *= x
#   return result
#
# def product_gradient(inputs):
#   return [ product(inputs[:i]+inputs[i+1:])
#            for i in range(len(inputs)) ]
#
# ADD = (sum, sum_gradient)
# MUL = (product, product_gradient)
#
# trinome = Network()
# one = trinome.node( None, [] )
# x   = trinome.node( None, [] )
# x_2 = trinome.node( MUL, [x, x] )
# _3x = trinome.node( ADD, [x, x, x] )
# _2_ = trinome.node( ADD, [one, one] )
# result = trinome.node( ADD, [x_2, _3x, _2_] )
# values = trinome.values([(one, 1), (x, 5)])
#
# print(trinome.derivatives(values, result))
# ## [ 2, 13, 1, 1, 1, 1 ]
#
# print(trinome.derivatives(values, x_2))
# ## [ 0, 10, 1, 0, 0, 0 ]

# foo = Network()
# node0 = foo.node(MUL, [])
# node3 = foo.node(MUL, [node0])
# node2 = foo.node(MUL, [node0])
# node1 = foo.node(MUL, [node0])
# node5 = foo.node(MUL, [node2, node1])
# node4 = foo.node(MUL, [node3, node5])
# values = foo.values([(0,1), (1, 5)])
# print(product_gradient(values))

import sys
exec(sys.stdin.read())