#!/usr/bin/env python3

class Graph:

    def __init__(self):
        self.nodes = {}
        self.edges_fwd = {}
        self.edges_rev = {}

    def add_node(self, k, **kwargs):
        self.nodes[k] = kwargs

    def add_edge(self, k1, k2, **kwargs):
        self.edges_fwd.setdefault(k1, {})[k2] = kwargs
        self.edges_rev.setdefault(k2, {})[k1] = kwargs

    def get_upstream_nodes(self, k):
        return list(self.edges_rev.get(k, {}))

    def get_downstream_nodes(self, k):
        return list(self.edges_fwd.get(k, {}))

def topo_sort(g):
    dep_nodes = {}
    indep_nodes = []

    for k in g.nodes:
        n_deps = len(g.get_upstream_nodes(k))
        if n_deps == 0:
            indep_nodes.append(k)
        else:
            dep_nodes[k] = n_deps

    while indep_nodes:
        k = indep_nodes.pop(0)
        yield k

        for k2 in g.get_downstream_nodes(k):
            dep_nodes[k2] -= 1
            if dep_nodes[k2] == 0:
                del dep_nodes[k2]
                indep_nodes.append(k2)

    if dep_nodes:
        raise ValueError('cycle detected')

g = Graph()
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')

g.add_edge('A', 'B')
g.add_edge('C', 'D')

print(list(topo_sort(g)))



