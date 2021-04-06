"""
    Project: CSC-445 - Algorithms
    Author: Ryan Clendenning, Kamylo Ramirez

    This file contains Queue data structure
    for the Layer 2 & Layer 3 topologies.

"""

import graphs


class PriorityQueue(object):
    def __init__(self, root: graphs.Node, priority: int):
        self.items = [(root, priority)]

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def insert(self, item: graphs.Node, priority: int):
        for i in range(len(self.items) - 1, -1, -1):
            print(self.items[i][1])
            if self.items[i][1] <= priority:
                self.items.insert(i + 1, (item, priority))
                break
