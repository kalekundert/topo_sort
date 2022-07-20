#!/usr/bin/env python3

class Heap:
    """
    A container that always provides constant-time access to its lowest-value 
    item.  Insertions and deletions are O(log(N)).
    """

    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)
        balance_up(self.items, len(self.items) - 1)

    def pop(self):
        item = self.items[0]
        self.items[0] = self.items[-1]
        self.items = self.items[:-1]
        if self.items:
            balance_down(self.items, 0)
        return item

def balance_up(items, j):
    """
    Modify the given *items* list in place to restore the heap property.

    The algorithm begins at the given child index *j* and recursively moves 
    towards the root node, flipping any items that are out of order.  This 
    process runs in O(log(N)) time, and requires that all of the items except 
    *j* are in heap order.
    """
    # i: parent; j: child
    if j == 0:
        return

    i = (j - 1) // 2

    if items[i] > items[j]:
        items[i], items[j] = items[j], items[i]
        balance_up(items, i)

def balance_down(items, i):
    """
    Modify the given *items* list in place to restore the heap property.

    The algorithm begins at the given parent index *i*, compares that item to 
    both of its children, then swaps the items as necessary to put them all in 
    heap order (i.e. to make the parent the smallest).  It then continues 
    recursively towards the leaf nodes.  This process runs in O(log(N)) time, 
    and requires that all of the items except *j* are in heap order.
    """
    n = len(items)
    j1 = 2*i + 1
    j2 = j1 + 1

    if j2 >= n:
        if j1 >= n:
            return
        else:
            j = j1
    else:
        j = j1 if items[j1] < items[j2] else j2

    if items[i] > items[j]:
        items[i], items[j] = items[j], items[i]
        balance_down(items, j)

