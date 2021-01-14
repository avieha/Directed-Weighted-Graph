import time
import matplotlib.pyplot as plt


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
def connected_components_test_nx(x:nx.DiGraph):
    start = time.time()
    g = nx.strongly_connected_components(x)
    #for i in g:
     #   print(i)
    end = time.time()

    return end - start


def connected_components_test(x:GraphAlgo):
    start = time.time()
    x.connected_components()
    end = time.time()
    return end - start

def plot():
    labels = ['shortest path', 'G2', 'G3', 'G4', 'G5','G6', 'G7', 'G8', 'G9', 'G10','G11', 'G12', 'G13', 'G14', 'G15','G16', 'G17', 'G18', 'G19', 'G20',
              'G21', 'G22', 'G23', 'G24', 'G25','G26', 'G27', 'G28', 'G29', 'G30']
    java = [0.022, 0.001, 0.001, 0, 0,0.022,0.002,0.004,0.003,0.002,0.077,0.012,0.042,0.014,0.031,0.296,0.045,0.149,0.138,0.358,
            0.458,0.172,0.315,0.235,1.636,0.52,0.136,0.42,0.281,5.155]
    py_our = [0,0,0,0,0,0.001,0.001,0.002011,0.002017,0.003,0.0156,0.0156,0.0156,0.0384,0.0477,0.237,0.237,0.3476,0.4236,1.7212,
              0.4848,0.4848,0.8483,0.9315,9.5603,0.745,0.7845,1.357,1.4571,28.3875]
    py_nx =[]
    width = 0.35 # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()

    ax.bar(labels, java, width, label='java')
    ax.bar(labels, py_our, width, bottom=java,
           label='python-our project')
    plt.axis([0,32,0,5])
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.legend()

    plt.show()


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
   # print("Graph: G_30000_2400000_1.json ")
   # print("time: ",shortest_path(x))
   # print("time: ",shortest_path_nx(y))
   # print("connected component time:[0,1] ",connected_component_test(x))
    print("connected_components_test")
    #print("time: ",connected_components_test(x))
    #print(x.connected_components())
    print("-----------------")
    #plot()
    print(connected_components_test_nx(y))

