import time

from pack.GraphAlgo import GraphAlgo
from pack.DiGraph import DiGraph
import networkx as nx

def shortest_path(x: GraphAlgo):
    start = time.time()
    x.shortest_path(0,1)
    end = time.time()
    print("our shortest path")
    print(x.shortest_path(0,1))
    return end-start

def shortest_path_nx(y: nx.DiGraph):
    start = time.time()
    nx.dijkstra_path(y,0,1)
    end = time.time()
    print("nx shortest path")
    print( nx.dijkstra_path(y,0,1))
    return end - start

def connected_component_test(x:GraphAlgo):
    start = time.time()
    x.connected_component(0)
    end = time.time()
    start2 = time.time()
    x.connected_component(1)
    end2 = time.time()
    return [end - start, end2-start2]


def connected_components_test(x:GraphAlgo):
    start = time.time()
    x.connected_components()
    end = time.time()
    return end - start











if __name__ == '__main__':
    x = GraphAlgo()  # type: GraphAlgo
    x.load_from_json('../data/G_30000_240000_1.json')
    y = nx.DiGraph()
    for node in x.g.get_all_v().values():
        y.add_node(node.id)
    for n in x.g.get_all_v().values():
        for edge in x.g.all_out_edges_of_node(n.id).values():
            u = n.id
            v = edge[0].id
            w = edge[1]
            y.add_weighted_edges_from([(u,v,w)])
    print("Graph: G_30000_2400000_1.json ")
    print("time: ",shortest_path(x))
    print("time: ",shortest_path_nx(y))
    print("connected component time:[0,1] ",connected_component_test(x))
    print("connected_components_test")
    print("time: ",connected_components_test(x))
