# imports
import graphs
import time
import sys


# Prim's Algorithm
def prims(graph: graphs.Graph, root: int):
    mst = [graph.nodes[root]]
    graph.nodes[root].visited = True
    while len(mst) < len(graph.nodes):
        min_dist = [graph.nodes[root], sys.maxsize]
        for _ in range(len(mst)):
            for _node in mst[_].neighbors:
                if _node[0].visited is False and _node[1] < min_dist[1]:
                    min_dist = _node
        min_dist[0].visited = True
        mst.append(min_dist[0])
    graph.reset()
    return mst


# Dijkstra's Algorithm
def dijkstras(graph: graphs.Graph, root: graphs.Node, target: graphs.Node):
    q = []
    dist = {}
    prev = {}
    for v in graph.nodes:
        dist[v] = sys.maxsize
        prev[v] = sys.maxsize
        q.append(v)
    dist[root] = 0
    while len(q) != 0:
        # u = list(dist.keys())[list(dist.values()).index(min(dist.values()))]
        u = graphs.Node
        closest = sys.maxsize
        for j in range(len(q)):
            if dist[q[j]] < closest:
                u = q[j]
                closest = dist[q[j]]
        if target == u:
            dist = sorted(dist.items(), key=lambda x: x[1])
            return dist, prev

        q.remove(u)
        for v in u.neighbors:
            if v[0] in q:
                alt = dist[u] + v[1]
                if alt < dist[v[0]]:
                    dist[v[0]] = alt
                    prev[v[0]] = u

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
