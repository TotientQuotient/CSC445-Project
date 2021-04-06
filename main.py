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
        for i in range(len(mst)):
            for _node in mst[i].neighbors:
                if _node[0].visited is False and _node[1] < min_dist[1]:
                    min_dist = _node
        min_dist[0].visited = True
        mst.append(min_dist[0])
    return mst


# main function of the program
if __name__ == '__main__':
    # executes if no runtime errors occurred
    print('Program successfully executed.\nTerminating now...')
    time.sleep(2)
    sys.exit(0)
