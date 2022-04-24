#!/usr/bin/env python3
class BridgeWalk(object):
  def __init__(self, graph):
    self.graph = graph
    self.bridges = {}
    self.maxpath = []

    for node in self.graph:
      for fork in self.graph[node]:
        for bridge in fork[1]:
          self.bridges[bridge] = 1

  def explore(self):
    # try different start nodes
    for node in self.graph:
      self.scan(node)

  def scan(self, node, path=[], seen={}):
    # try different connected nodes
    for fork in self.graph[node]:
      # try all bridges leading there
      for bridge in fork[1]:
        self.bridge_ok(bridge, fork[0], path.copy(), seen.copy())

  def bridge_ok(self, bridge, node, path, seen):
    print(bridge, node, path, seen)
    if not bridge in seen:
      seen[bridge] = 1
      path.append(bridge)

      if len(self.maxpath) < len(path):
        self.maxpath = path.copy()

      # recurse
      self.scan(node, path, seen)
