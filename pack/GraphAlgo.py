import json
import queue
from typing import List
from DiGraph import DiGraph
from pack.GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self):
        self.g = DiGraph()

    def get_graph(self):
        return self.g

    def load_from_json(self, file_name: str):
        new_graph = DiGraph()
        with open(file_name, 'r') as fp:
            jsn = json.load(fp)
        for item in jsn['nodes']:
            new_graph.add_node(item.get('id'))
        for edge in jsn['edges']:
            src = edge['src']
            dest = edge['dest']
            w = edge['w']
            new_graph.add_edge(src, dest, w)
        return new_graph

    def save_to_json(self, filename):
        x = []
        y = []
        for key, value in self.g.get_all_v().items():
            if value.pos is None:
                x.append({"id": value.id})
            else:
                x.append({"id": value.id, "pos": value.pos})
        for key, value in self.g.get_all_v().items():
            for sec_key, sec_val in self.g.all_out_edges_of_node(value.id).items():
                y.append({"src": value.id, "dest": sec_val[0].id, "w": sec_val[1]})
        w = {}
        w["nodes"] = x
        w["edges"] = y
        with open(filename, 'w') as json_file:
            json.dump(w, json_file)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if self is None:
            return (-1, [])
        if self.g.get_node(id1) is None or self.g.get_node(id2) is None:
            return (-1, [])
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
                    sum = node.w+self.g.get_edge(node.id, ni_node[0].id)
                    if sum < self.g.get_node(ni_node[0].id).w or self.g.get_node(ni_node[0].id).w == -1:
                        self.g.get_node(ni_node[0].id).w=sum
                        dict_node[ni_node[0].id]=node.id
                        q.put( ni_node[0])
        arr_list = []
        if self.g.get_node(id2).w == -1:
            return (-1, ())
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

    def connected_component(self, id1: int):
        if self.g is None or self.g.get_node(id1) is None:
            return []
        self.DFS(self.g.get_node(id1))
        visited = []
        for node in self.g.get_all_v().values():
            if node.tag == 1:
                visited.append(node.id)
        graph.g = self.reverse_graph(self.g)
        graph.DFS(graph.g.get_node(id1))
        list = []
        for node in self.g.get_all_v().values():
            if node.tag == 1 and node.id in visited:
                list.append(node.id)
        return list

    def reverse_graph(self, graph):
        graph2 = DiGraph()
        for node in graph.get_all_v().keys():
            graph2.add_node(node)
        for ver in graph.get_all_v().values():
            for edge in graph.all_out_edges_of_node(ver.id).values():
                graph2.add_edge(edge[0].id, ver.id, 0)
        return graph2

    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):
        for key, node in self.g.get_all_v().items():
            node.tag = 0
        self.DFSUtil(v)

        # A function used by DFS
    def DFSUtil(self, v):
        # Mark the current node as visited
        # and print it
        v.tag = 1
        # Recur for all the vertices
        # adjacent to this vertex
        for key, neighbour in self.g.all_out_edges_of_node(v.id).items():
            if neighbour[0].tag == 0:
                self.DFSUtil(neighbour[0])

    def connected_components(self):
        list = []
        for vertex in self.g.get_all_v().values():
            if self.connected_component(vertex.id) not in list:
               list.append(self.connected_component(vertex.id))
        return list

    def plot_graph(self):
        pass


if __name__ == '__main__':
    graph = GraphAlgo()
    graph.get_graph().add_node(1, None)
    graph.get_graph().add_node(2, None)
    graph.get_graph().add_node(3, None)
    graph.get_graph().add_node(4, None)
    graph.get_graph().add_node(5, None)
    graph.get_graph().add_node(6, None)
    graph.get_graph().add_edge(1, 2, 3.5)
    graph.get_graph().add_edge(1, 3, 5)
    graph.get_graph().add_edge(1, 6, 6)
    graph.get_graph().add_edge(2, 4, 4)
    graph.get_graph().add_edge(2, 5, 7)
    graph.get_graph().add_edge(3, 4, 1)
    graph.get_graph().add_edge(4, 1, 3)
    graph.get_graph().add_edge(6, 1, 2.3)
    # graph.get_graph().add_edge(6, 2, 2.3)
    # graph.get_graph().remove_edge(1, 2)
    # graph.save_to_json("test_json")
    # x = graph.load_from_json("test_json")
    # print(graph.get_graph())
    # print(graph.get_graph().get_node(2).ni_out)
    # graph.get_graph().remove_edge(1, 3)
    # print("first graph", graph.get_graph())
    # print("sec graph", x)
    print(graph.connected_components())
    # y = graph.shortest_path(1, 9)
    # print(y)
