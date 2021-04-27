"""
    Project: CSC-445 - Algorithms
    Author: Ryan Clendenning, Kamylo Ramirez

    This file contains Graph and Node data
    structures for the Layer 2 & Layer 3 topologies.

"""

# imported libraries
import random


# define the Node class utilized in the Graph class
class Node(object):
    def __init__(self, name: int, data: str):
        self.name = name
        self.data = data
        self.neighbors = []
        self.visited = False
        self.initialized = False

    def set_visited(self, value: bool):
        self.visited = value


# define the Graph class and its functions
class Graph(object):
    def __init__(self, node_num: int):
        self.node_num = node_num
        self.nodes = [Node(-1, '') for _ in range(node_num)]

    # method for removing non-inserted Node locations
    def clean(self):
        for node in self.nodes:
            if node.initialized is False:
                self.nodes.remove(node)

    # method for resetting the attribute values post algorithm
    def reset(self):
        for node in self.nodes:
            node.visited = False

    # method for inserting Nodes into the graph
    def insert_node(self, name: int, data: str):
        self.nodes[name] = Node(name, data)
        self.nodes[name].initialized = True

    def get_node_neighbors(self, n: int, x=False):
        if x is False:
            return self.nodes[n].neighbors
        else:
            for m in self.nodes[n].neighbors:
                print(m.name)

    # method for linking two Nodes together with neighbors_2
    def add_neighbor(self, n: int, m: int, w: int):
        if self.nodes[m] not in self.nodes[n].neighbors and self.nodes[n] not in self.nodes[m].neighbors:
            self.nodes[n].neighbors.append([self.nodes[m], w])
            self.nodes[m].neighbors.append([self.nodes[n], w])


# method for creating complete graphs for generic testing
def gen_complete_graph(num_node: int):
    graph = Graph(num_node)
    for i in range(num_node):
        graph.insert_node(i, str(i))
        if i != 0:
            for j in range(i):
                graph.add_neighbor(i, j, random.randint(1, 15))
    graph.clean()
    return graph


# method for creating & returning a graph based on a graph.csv file
def base_graph(file_name: str):
    with open(file_name, 'r') as file:
        nodes = file.read().split('\n')
    graph = Graph(len(nodes))
    for i in range(len(nodes)):
        n = nodes[i].split(', ')
        graph.insert_node(int(n[0]), n[1])
        if i != 0:
            for j in range(i):
                graph.add_neighbor(i, j, random.randint(1, 15))
    graph.clean()
    return graph


# method to create the graph used by GeeksForGeeks' algorithm explanation
def gen_gfg_graph():
    graph = Graph(9)

    # create the nodes for the graph
    graph.insert_node(0, '0')
    graph.insert_node(1, '1')
    graph.insert_node(2, '2')
    graph.insert_node(3, '3')
    graph.insert_node(4, '4')
    graph.insert_node(5, '5')
    graph.insert_node(6, '6')
    graph.insert_node(7, '7')
    graph.insert_node(8, '8')

    # connect the nodes
    graph.add_neighbor(0, 1, 4)
    graph.add_neighbor(0, 7, 8)
    graph.add_neighbor(1, 2, 8)
    graph.add_neighbor(1, 7, 11)
    graph.add_neighbor(7, 8, 7)
    graph.add_neighbor(7, 6, 1)
    graph.add_neighbor(2, 3, 7)
    graph.add_neighbor(2, 8, 2)
    graph.add_neighbor(2, 5, 4)
    graph.add_neighbor(6, 8, 6)
    graph.add_neighbor(6, 5, 2)
    graph.add_neighbor(5, 4, 10)
    graph.add_neighbor(5, 3, 14)
    graph.add_neighbor(3, 4, 9)

    return graph


def gen_programiz_graph():
    graph = Graph(6)

    # Create the nodes for the graph
    graph.insert_node(0, 'A')
    graph.insert_node(1, 'B')
    graph.insert_node(2, 'C')
    graph.insert_node(3, 'D')
    graph.insert_node(4, 'E')
    graph.insert_node(4, 'F')

    # Connect the nodes
    graph.add_neighbor(0, 1, 4)
    graph.add_neighbor(0, 2, 2)
    graph.add_neighbor(1, 2, 4)
    graph.add_neighbor(2, 3, 1)
    graph.add_neighbor(2, 4, 6)
    graph.add_neighbor(2, 5, 3)
    graph.add_neighbor(3, 4, 3)
    graph.add_neighbor(4, 5, 2)

    return graph
