#!/usr/bin/env python3

from heap import Heap

class Graph:
    """
    A collection of nodes connected by directed edges.

    Nodes can be any hashable object.  Arbitrary key/value pairs can be 
    associated with each node and edge.  The underlying data structure is an 
    adjacency list, which allows for constant-time insertions, deletions, and 
    look-ups.
    """

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
    """
    Yield the nodes of the given directed graph such that (i) each node comes 
    after all of its ancestors and (ii) in sorted order otherwise.
    """
    dep_nodes = {}
    indep_nodes = Heap()

    for k in g.nodes:
        n_deps = len(g.get_upstream_nodes(k))
        if n_deps == 0:
            indep_nodes.push(k)
        else:
            dep_nodes[k] = n_deps

    while indep_nodes:
        k = indep_nodes.pop()
        yield k

        for k2 in g.get_downstream_nodes(k):
            dep_nodes[k2] -= 1
            if dep_nodes[k2] == 0:
                del dep_nodes[k2]
                indep_nodes.push(k2)

    if dep_nodes:
        raise ValueError('cycle detected')

