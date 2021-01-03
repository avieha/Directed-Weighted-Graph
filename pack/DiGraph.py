class DiGraph:

    def __init__(self):
        self.nodes = {}
        self.mc = 0
        self.edgesize = 0

    def v_size(self):
        return len(self.nodes)

    def e_size(self):
        return self.edgesize

    def get_all_v(self):
        return self.nodes

    def all_in_edges_of_node(self, id1: int):
        x = self.nodes.get(id1)
        x = Node(x)
        return x.ni_in

    def all_out_edges_of_node(self, id1: int):
        x = self.nodes.get(id1)
        x = Node(x)
        return x.ni_out

    def get_mc(self):
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float):
        x = Node(self.get_node(id1))
        y = Node(self.get_node(id2))
        if x or y is None:
            return False
        if x.ni_out[id2] is None:
            y.ni_in[id1] = [self.get_node(id1), weight]
            x.ni_out[id2] = [self.get_node(id2), weight]
            self.mc += 1
        else:
            curr_weight = list[x.ni_out[id2]][1]
            if curr_weight is not weight:
                self.mc += 1
            y.ni_in[id1] = [self.get_node(id1), weight]
            x.ni_out[id2] = [self.get_node(id2), weight]
        return True

    def get_node(self, id1):
        if self.nodes.get(self, id1) is None:
            return None
        return self.nodes.get(self, id1)

    def add_node(self, node_id: int, pos: tuple = None):
        x = self.get_node(node_id)
        if x is not None:
            return False
        x = Node(node_id, pos)
        self.nodes[node_id] = x
        self.mc += 1
        return True

    def remove_node(self, node_id: int):
        x = self.get_node(node_id)
        if x is not None:
            return False
        arr_in = Node(x).ni_in
        arr_out = Node(x).ni_out
        for edge_in in arr_in.keys():
            w = Node(self.get_node(self, edge_in))
            w.ni_out.pop(self, node_id)
        for edge_out in arr_out.keys():
            r = Node(self.get_node(self, edge_out))
            r.ni_in.pop(self, node_id)
            self.edgesize -= 1
            self.mc += 1
        self.nodes.pop(self, node_id)
        self.mc += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int):
        x = Node(node_id1)
        if x.get_edge(self, node_id2) is False:
            return False
        x.ni_out.pop(self, node_id2)
        self.get_node(node_id2).ni_in.pop(self, node_id1)
        self.mc -= 1
        self.edgesize -= 1
        return True

    def __str__(self):
        for node_in in self.nodes.keys():
            print(node_in)
        return ''


class Node:

    def __init__(self, key, pos):
        self.id = key
        self.tag = 0
        self.info = ''
        self.pos = pos
        self.ni_in = {}
        self.ni_out = {}

    def get_edge(self, id1):
        if self.ni_out.get(self, id1) is None:
            return False
        return True


if __name__ == '__main__':
    graph = DiGraph()
    graph.add_node(1, None)
    graph.add_node(2, None)
    graph.add_node(3, None)
    graph.add_node(4, None)
    # graph.add_edge(1, 2, 3.5)
    # graph.add_edge(2, 4, 5)
    # graph.add_edge(1, 3, 1)
    print(graph)
