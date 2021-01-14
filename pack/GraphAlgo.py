import json
import queue

from pack.DiGraph import DiGraph
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
import random

from pack.GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    """
     * this class implements "GraphAlgoInterface" and lets us take a DiGraph and make over it some
     manipulations like:
     * 1. init(graph);
     * 2. Connected_component(int id); // around specific node
     * 3. connected_components();
     * 4. shortestPath(int src, int dest);
     * 5. Save to JSon(file);
     * 6. Load from JSon(file);
     * 7. Plot the graph; """

    """this method init the DWGraph_algo over the received DWGraph so we can run
         all the function of this class over the graph"""
    def __init__(self, d_graph=None):
        if d_graph is None:
            self.g = DiGraph()
        else:
            self.g = d_graph

    """this method return the graph we init"""
    def get_graph(self):
        return self.g

    """this method loads a graph from saved JSON file
    and deserializes it into a DiGraph
    :param file_name - the file's address"""
    def load_from_json(self, file_name: str):
        if self is None:
            return False
        new_graph = DiGraph()
        try:
            with open(file_name, 'r') as fp:
                jsn = json.load(fp)
            for item in jsn['Nodes']:
                new_graph.add_node(item.get('id'))
                if item.get('pos') is not None:
                    pos = item.get('pos')
                    x, y, z = pos.split(',')
                    x = float(x)
                    y = float(y)
                    z = float(z)
                    new_graph.get_node(item.get('id')).pos = (x, y, z)
            for edge in jsn['Edges']:
                src = edge['src']
                dest = edge['dest']
                w = edge['w']
                new_graph.add_edge(src, dest, w)
            self.g = new_graph
        except:
            print('cant open file')
            return False
        return True

    """a method to save the graph as a json
     * we made a json String of the graph and saved it in a file
     * :param filename - the file name(may include a relative path)"""
    def save_to_json(self, filename):
        if self is None or self.g is None:
            return False
        x = []
        y = []
        try:
            for key, value in self.g.get_all_v().items():
                if value.pos is None:
                    x.append({"id": value.id})
                else:
                    s, t, u = value.pos
                    str_pos = str(s) + ", " + str(t) + ", " + "0.0"
                    x.append({"id": value.id, "pos": str_pos})
            for key, value in self.g.get_all_v().items():
                for sec_key, sec_val in self.g.all_out_edges_of_node(value.id).items():
                    y.append({"src": value.id, "dest": sec_val[0].id, "w": sec_val[1]})
            w = {}
            w["Nodes"] = x
            w["Edges"] = y
            with open(filename, 'w') as json_file:
                json.dump(w, json_file)
        except:
            print('Error saving file')
            return False
        return True

    """this method return a list of the shortest path between 2 nodes.
     * for every node we keep the node where we came from and this allows us to return a list 
     of the shortest path we used a dictionary which keep 
     for every node the node which was before him in that way we can go to the dest node and check 
     which node is before him and we can go like this until we get the
     src node then we just need to reverse the list and we're done
     * :param src  - start node
     * :param dest - end (target) node
     * :return tuple """
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if self is None or self.g is None:
            return (float('inf'), [])
        if self.g.get_node(id1) is None or self.g.get_node(id2) is None:
            return (float('inf'), [])
        if id1 == id2:
            return (0, [id1])
        for key, node in self.g.get_all_v().items():
            node.w = -1
            node.tag = 0
        q = queue.PriorityQueue()
        dict_node = {}
        node = self.g.get_node(id1)
        node.w = 0
        q.put(node)
        while not q.empty():
            node = q.get()
            node.tag = 1
            ni_list = self.g.all_out_edges_of_node(node.id)
            for key, ni_node in ni_list.items():
                if self.g.get_node(ni_node[0].id).tag == 0:
                    sum = node.w + self.g.get_edge(node.id, ni_node[0].id)
                    if sum < self.g.get_node(ni_node[0].id).w or self.g.get_node(ni_node[0].id).w == -1:
                        self.g.get_node(ni_node[0].id).w = sum
                        dict_node[ni_node[0].id] = node.id
                        q.put(ni_node[0])
        arr_list = []
        if self.g.get_node(id2).w == -1:
            return (float('inf'), [])
        else:
            prev_node = id2
            arr_list.append(prev_node)
            prev_node = dict_node.get(prev_node)
            while prev_node != id1:
                arr_list.append(prev_node)
                prev_node = dict_node.get(prev_node)
            arr_list.append(id1)
            arr_list.reverse()
        tuple_list = (self.g.get_node(id2).w, arr_list)
        return tuple_list

    """ in this method we uses DFS algorithm twice in order to find strongly connected components
    around a specific node, the list we return contains the relevant items for the id given
    :param id1 - the desired node id
    :return list """
    def connected_component(self, id1: int):
        if self.g is None or self.g.get_node(id1) is None:
            return []
        graph = GraphAlgo()
        self.DFS(self.g.get_node(id1))
        graph.g = self.reverse_graph(self.g)
        graph.DFS(graph.g.get_node(id1))
        list = []
        for node in graph.g.get_all_v().values():
            if node.tag == 1 and self.g.get_node(node.id).tag == 1:
                list.append(node.id)
        return list

    """a method in use from reversing the graph in the CC search
    :param graph - original graph
    :return reversed version of the graph"""
    def reverse_graph(self, graph):
        graph2 = DiGraph()
        for node in graph.get_all_v().keys():
            graph2.add_node(node)
        for ver in graph.get_all_v().values():
            for edge in graph.all_out_edges_of_node(ver.id).values():
                graph2.add_edge(edge[0].id, ver.id, 0)
        return graph2

    """ The function to do DFS iterative traversal
     :param v - starting node to make DFS from"""
    def DFS(self, v):
        for node in self.g.get_all_v().values():
            node.tag = 0
        q = queue.LifoQueue(maxsize=0)
        v.tag = 1
        q.put_nowait(v)
        while not q.empty():
            v = q.get()
            for neighbour in self.g.all_out_edges_of_node(v.id).values():
                if neighbour[0].tag == 0:
                    neighbour[0].tag = 1
                    q.put(neighbour[0])

    """ this method iterate over the graph and at every unvisited node calls connected_component(this node)
    and stores all existing strongly connected items in the graph at one list
    :return list """
    def connected_components(self):
        list = []
        for ver in self.g.get_all_v().values():
            ver.w = -1
        for vertex in self.g.get_all_v().values():
            if vertex.w == 1:
                continue;
            list2 = self.connected_component(vertex.id)
            for i in list2:
                self.g.get_node(i).w = 1
            list.append(list2)
        return list

    """this method plots the graph using matplotlib and visualizes the graph - if no position stored at
    a node - randomizes location"""
    def plot_graph(self):
        x = []
        y = []
        n = []
        max_x = -1000
        min_x = 1000
        max_y = -1000
        min_y = 1000
        for node in self.g.get_all_v().values():
            n.append(node.id)
            if node.pos is None:
                node.pos = (int(random.randrange(0, 100, 3)), int(random.randrange(0, 100, 8)), 0)
            x.append(node.pos[0])
            y.append(node.pos[1])
            if node.pos[0] > max_x:
                max_x = node.pos[0]
            if node.pos[1] > max_y:
                max_y = node.pos[1]
            if node.pos[0] < min_x:
                min_x = node.pos[0]
            if node.pos[1] < min_y:
                min_y = node.pos[1]
        fig, ax = plt.subplots(facecolor=(0.5, 0.8, 0.8))
        ax.scatter(x, y, 100, 'red')
        for ver in self.g.get_all_v().values():  # type Node
            for neighbour in self.g.all_out_edges_of_node(ver.id).values():
                from_xy = (ver.pos[0], ver.pos[1])
                to_xy = (neighbour[0].pos[0], neighbour[0].pos[1])
                con = ConnectionPatch(from_xy, to_xy, "data", "data",
                                      arrowstyle="-|>", shrinkA=5, shrinkB=5,
                                      mutation_scale=18, fc="orange")
                ax.add_artist(con)
                # plt.annotate('', to_xy, from_xy ,arrowprops=dict(headwidth=5, width=0.5, shrink=0.07),)
        for i, txt in enumerate(n):
            ax.annotate(txt, (x[i], y[i] + 0.0002))
        ax.text(0.5, 0.5, 'created by aviem and amiel', transform=ax.transAxes,
                fontsize=30, color='gray', alpha=0.5,
                ha='center', va='center', rotation='30')
        plt.axis([min_x - 0.001, max_x + 0.001, min_y - 0.001, max_y + 0.001])
        # plt.axis([0, 100, 0, 100])
        plt.xlabel('X axis')
        plt.ylabel('Y axis')
        ax.set_facecolor('#eafff5')
        ax.set_title('Directed Weighted Graph')
        plt.show()

    """transforms the GraphAlgo object into something we can read"""
    def __str__(self):
        print(self.g)
        return ""
