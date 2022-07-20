#!/usr/bin/env python3

import pytest
from topo_sort import *

def test_topo_sort_A():
    g = Graph()
    g.add_node('A')

    assert list(topo_sort(g)) == ['A']

def test_topo_sort_AB():
    g = Graph()
    g.add_node('A')
    g.add_node('B')
    g.add_edge('A', 'B')

    assert list(topo_sort(g)) == ['A', 'B']

def test_topo_sort_BA():
    g = Graph()
    g.add_node('B')
    g.add_node('A')
    g.add_edge('B', 'A')

    assert list(topo_sort(g)) == ['B', 'A']

def test_topo_sort_AB_BA():
    g = Graph()
    g.add_node('A')
    g.add_node('B')
    g.add_edge('A', 'B')
    g.add_edge('B', 'A')

    with pytest.raises(ValueError, match='cycle detected'):
        list(topo_sort(g))

def test_topo_sort_AB_AC():
    g = Graph()
    g.add_node('A')
    g.add_node('B')
    g.add_node('C')
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')

    assert list(topo_sort(g)) == ['A', 'B', 'C']

def test_topo_sort_AC_AB():
    g = Graph()
    g.add_node('C')
    g.add_node('B')
    g.add_node('A')
    g.add_edge('A', 'C')
    g.add_edge('A', 'B')

    assert list(topo_sort(g)) == ['A', 'B', 'C']

def test_topo_sort_AB_CD():
    g = Graph()
    g.add_node('A')
    g.add_node('B')
    g.add_node('C')
    g.add_node('D')
    g.add_edge('A', 'B')
    g.add_edge('C', 'D')

    assert list(topo_sort(g)) == ['A', 'B', 'C', 'D']

def test_topo_sort_CD_BA():
    g = Graph()
    g.add_node('D')
    g.add_node('C')
    g.add_node('B')
    g.add_node('A')
    g.add_edge('C', 'D')
    g.add_edge('A', 'B')

    assert list(topo_sort(g)) == ['A', 'B', 'C', 'D']

