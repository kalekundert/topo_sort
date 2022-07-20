#!/usr/bin/env python3

import pytest
from heap import *
from hypothesis import given, settings
from hypothesis.strategies import lists, integers

@pytest.mark.parametrize(
        'items, j, expected', [
            ([0], 0, [0]),

            ([0,1], 1, [0,1]),
            ([1,0], 1, [0,1]),
            
            ([0,1,2], 2, [0,1,2]),
            ([0,2,1], 2, [0,2,1]),
            ([1,2,0], 2, [0,2,1]),

            ([0,1,2,3], 3, [0,1,2,3]),
        ]
)
def test_balance_up(items, j, expected):
    balance_up(items, j)
    assert items == expected

@pytest.mark.parametrize(
        'items, i, expected', [
            ([0], 0, [0]),

            ([0,1], 0, [0,1]),
            ([1,0], 0, [0,1]),

            ([0,1,2], 0, [0,1,2]),
            ([0,2,1], 0, [0,2,1]),
            ([1,0,2], 0, [0,1,2]),
            ([1,2,0], 0, [0,2,1]),
            ([2,0,1], 0, [0,2,1]),
            ([2,1,0], 0, [0,1,2]),
        ],
)
def test_balance_down(items, i, expected):
    balance_down(items, i)
    assert items == expected

@given(lists(integers(), min_size=1))
@settings(deadline=None)
def test_heap(items):
    h = Heap()
    n = len(items)

    assert len(h) == 0

    for i, item in enumerate(items):
        h.push(item)
        assert len(h) == i + 1

    for i, expected in enumerate(sorted(items)):
        item = h.pop()
        assert item == expected
        assert len(h) == n - i - 1
