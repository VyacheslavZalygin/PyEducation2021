class Foo:
  def __init__(self, value):
    self.value = value

  def add(self, foo):
    return Foo(self.value+foo.value)

import sys
exec(sys.stdin.read())