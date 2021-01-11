from pack.GraphInterface import GraphInterface


class DiGraph:

    def __init__(self):
        self.nodes = {}
        self.mc = 0
        self.edgesize = 0

    def v_size(self):
        if self is None:
            return 0
        return len(self.nodes)

    def e_size(self):
        if self is None:
            return 0
        return self.edgesize

    def get_all_v(self):
        if self is None:
            return None
        return self.nodes

    def all_in_edges_of_node(self, id1: int):
        if self is None or self.get_node(id1) is None:
            return None
        x = self.nodes.get(id1)
        return x.ni_in

    def all_out_edges_of_node(self, id1: int):
        if self is None or self.get_node(id1) is None:
            return None
        x = self.nodes.get(id1)
        return x.ni_out

    def get_mc(self):
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float):
        src = self.get_node(id1)
        dest = self.get_node(id2)
        if self is None or self.get_node(id1) is None or self.get_node(id2) is None or weight < 0:
            return False
        if dest is None or src is None:
           return False
        if id1 == id2:
            return False
        if src.ni_out.get(id2) is None:
            dest.ni_in[id1] = self.get_node(id1)
            src.ni_out[id2] = [self.get_node(id2), weight]
            self.mc += 1
            self.edgesize += 1
        else:
            return False
        return True

    def get_node(self, id1):
        if self is None:
            return None
        if self.nodes.get(id1) is None:
            return None
        return self.nodes.get(id1)

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
        if x is None:
            return False
        arr_in = x.ni_in
        arr_out = x.ni_out
        for edge_in in arr_in.values():
            edge_in.ni_out.pop(node_id)
            self.edgesize -= 1
            self.mc += 1
        for edge_out in arr_out.values():
            t = edge_out[0]
            t.ni_in.pop(node_id)
            self.edgesize -= 1
            self.mc += 1
        self.nodes.pop(node_id)
        self.mc += 1
        return True

    def get_edge(self, id1: int, id2: int):
        if self.nodes.get(id1) is None:
            return None
        list = self.all_out_edges_of_node(id1)
        if list.get(id2) is None:
            return None
        else:
            return list.get(id2)[1]

    def remove_edge(self, node_id1: int, node_id2: int):
        src = self.get_node(node_id1)
        if src is None:
            return False
        if src.get_edge(node_id2) is False:
            return False
        src.ni_out.pop(node_id2)
        self.get_node(node_id2).ni_in.pop(node_id1)
        self.mc += 1
        self.edgesize -= 1
        return True

    def __str__(self):
        print("nodes:{")
        for node_in in self.nodes.keys():
            print(node_in, end=" [")
            x = self.all_out_edges_of_node(node_in)
            length = len(x)
            counter = 0
            for y in x:
                if counter is length-1:
                  print(y, end="")
                else:
                    print(y, end=" , ")
                    counter += 1
            print("]")
        print("}")
        return ''

    def __eq__(self, other):
        if(len(self.get_all_v().values())!=len(other.get_all_v().values())):
            return False
        for node1 ,node2 in zip(self.get_all_v().values(), other.get_all_v().values()):
            if node1!=node2:
                return False
            if (len(self.all_out_edges_of_node(node1.id)) != len(other.all_out_edges_of_node(node2.id))):
                return False
            for in1, in2 in zip(self.all_out_edges_of_node(node1.id),other.all_out_edges_of_node(node2.id)):
                if in1!=in2:
                    return False
            if (len(self.all_in_edges_of_node(node1.id)) != len(other.all_in_edges_of_node(node2.id))):
                return False
            for out1, out2 in zip(self.all_in_edges_of_node(node1.id),other.all_in_edges_of_node(node2.id)):
                if out1!=out2:
                    return False

        return True
class Node:
    def __init__(self, key, pos):
        self.id = key
        self.tag = 0
        self.w = -1
        self.info = ''
        self.pos = pos
        self.ni_in = {}
        self.ni_out = {}

    def get_edge(self, id1):
        if self.ni_out.get(id1) is None:
            return False
        return True

    def __lt__(self, other):
        return self.w < other.w

    def __gt__(self, other):
        return self.w > other.w

    def __eq__(self, other):
        return self.w == other.w

    def __str__(self):
        print(self.id)
        return ''

    def __eq__(self, other):
        return self.id == other.id