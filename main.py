# imports
import graphs
import time
import sys


# Prim's Algorithm: This algorithm is used for STP in the Data-Link (2nd) Layer in the OSI Model.
def prims(graph: graphs.Graph, root: int):
    # define the initial mst set. Initially insert the root node and set the root node to visited
    mst = [graph.nodes[root]]
    graph.nodes[root].visited = True
    # Loop to determine if the mst set is filled.
    while len(mst) < len(graph.nodes):
        # This variable is to determining the closest non-visited node
        min_dist = [graph.nodes[root], sys.maxsize]
        # Nested loops to cycle through each node in _'s neighbors and determine
        # if the node is visited and less than the current value of min_dist
        for _ in range(len(mst)):
            for _node in mst[_].neighbors:
                if _node[0].visited is False and _node[1] < min_dist[1]:
                    min_dist = _node
        # Set the determined closest node to visited and append to the mst set.
        min_dist[0].visited = True
        mst.append(min_dist[0])
    # Resets nodes in graph to unvisited and returns the mst set
    graph.reset()
    return mst


# Dijkstra's Algorithm: This algorithm is used in the Network (3rd) Layer of the OSI Model.
def dijkstras(graph: graphs.Graph, root: graphs.Node, target: graphs.Node):
    # Define the variable sets for the algorithm. 
    q = []
    dist = {}
    prev = {}
    # Loop to fill the distance and previous dictionary sets with all nodes in graph to INF
    # then set the distance of root node to 0.
    for v in graph.nodes:
        dist[v] = sys.maxsize
        prev[v] = sys.maxsize
        q.append(v)
    dist[root] = 0
    # Loop to check if each node, until target is set, is removed from the q set.
    while len(q) != 0:
        # u = list(dist.keys())[list(dist.values()).index(min(dist.values()))]
        # Variables for determining which node to next add to the SPT.
        u = graphs.Node
        closest = sys.maxsize
        # Loop to determine the closest node in the graph.
        for j in range(len(q)):
            if dist[q[j]] < closest:
                u = q[j]
                closest = dist[q[j]]
        # If the current node is the target node, then return the distance and previous dictionary sets
        if target == u:
            dist = sorted(dist.items(), key=lambda x: x[1])
            return dist, prev
        # Remove the current node from the q set.
        q.remove(u)
        # Loop to set the respected distance and previous for the neighbors of the current node
        # if in the q set.
        for v in u.neighbors:
            if v[0] in q:
                alt = dist[u] + v[1]
                if alt < dist[v[0]]:
                    dist[v[0]] = alt
                    prev[v[0]] = u

    # Return the distance and previous dictionary sets.
    return dist, prev


# main function of the program
if __name__ == '__main__':
    g1 = graphs.gen_gfg_graph()

    print('Performing Prim\'s algorithm')
    g1_mst = prims(g1, 2)
    for node in g1_mst:
        print(node.name)

    time.sleep(1)
    print('\n\nPerforming Dijkstra\'s algorithm')

    g2 = graphs.gen_gfg_graph()
    g2_spt = dijkstras(g2, g2.nodes[2], g2.nodes[0])
    node_dist = g2_spt[0]
    node_prev = g2_spt[1]
    for i in range(len(node_dist)):
        if isinstance(node_prev[node_dist[i][0]], graphs.Node):
            print('Node name: {}, Previous Node: {}, Shortest Path Distance: {}'.format(node_dist[i][0].name,
                                                                                        node_prev[node_dist[i][0]].name,
                                                                                        node_dist[i][1]))
        else:
            print('Node name: {}, Previous Node: None, Shortest Path Distance: {}'.format(node_dist[i][0].name,
                                                                                          node_dist[i][1]))

    # executes if no runtime errors occurred
    print('Program successfully executed.\nTerminating now...')
    time.sleep(2)
    sys.exit(0)
