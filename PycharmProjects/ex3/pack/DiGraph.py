from pack.GraphInterface import GraphInterface


class DiGraph:
    #     this class represent a directed weighted graph
    def __init__(self):
        self.nodes = {}
        self.mc = 0
        self.edgesize = 0

    # method that return the size of vertices in the graph
    def v_size(self):
        return len(self.nodes)

    # method that return the size of the edges in the graph
    def e_size(self):
        return self.edgesize

    # methos that return a dictionary with all the nodes in the graph
    def get_all_v(self):
        return self.nodes

    # method that return a dictionary with all the nodes which have edges to the given node
    def all_in_edges_of_node(self, id1: int):
        if self is None or self.get_node(id1) is None:
            return None
        return self.get_node(id1).ni_in

    # method that return a dictionary with lists inside in the first index of the list there is a node which
    # is the neighboor of the given node in the second index of list is the weight of the edge
    def all_out_edges_of_node(self, id1: int):
        if self is None or self.get_node(id1) is None:
            return None
        return self.get_node(id1).ni_out

    # method to return the number of changes in the graph
    def get_mc(self):
        return self.mc

    # method to add an edge, the edge is added to the "in" dictionary of dest node and to out dictionery of src node
    def add_edge(self, id1: int, id2: int, weight: float):
        src = self.get_node(id1)
        dest = self.get_node(id2)
        if src is None or dest is None or weight < 0:
            return False
        if id1 == id2:
            return False
        if src.ni_out.get(id2) is None:
            dest.ni_in[id1] = weight
            src.ni_out[id2] = weight
            self.mc += 1
            self.edgesize += 1
        else:
            return False
        return True

    # our method to return a node
    def get_node(self, id1):
        if self.nodes.get(id1) is None:
            return None
        return self.nodes.get(id1)

    # method to add a node
    def add_node(self, node_id: int, pos: tuple = None):
        x = self.get_node(node_id)
        if x is not None:
            return False

        self.nodes[node_id] = Node(node_id, pos)
        self.mc += 1
        return True

    # method to remove a node also remove all the edges it is connected to
    def remove_node(self, node_id: int):
        x = self.get_node(node_id)
        if x is None:
            return False
        arr_in = x.ni_in
        arr_out = x.ni_out
        for edge_in in arr_in.keys():
            self.get_node(edge_in).ni_out.pop(node_id)
            self.edgesize -= 1
            self.mc += 1
        for edge_out in arr_out.keys():
            self.get_node(edge_out).ni_in.pop(node_id)
            self.edgesize -= 1
            self.mc += 1
        self.nodes.pop(node_id)
        self.mc += 1
        return True

    # our method to return an edge , return the weight
    def get_edge(self, id1: int, id2: int):
        if self.nodes.get(id1) is None:
            return None
        list = self.all_out_edges_of_node(id1)
        if list.get(id2) is None:
            return None
        else:
            return list.get(id2)

    # method to remove an edge between to nodes
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

    # method to print the graph nicely-
    def __str__(self):
       return repr(self)
        # print("nodes:{")
        # for node_in in self.nodes.keys():
        #     print(node_in, end=" [")
        #     x = self.all_out_edges_of_node(node_in)
        #     length = len(x)
        #     counter = 0
        #     for y in x:
        #         if counter is length - 1:
        #             print(y, end="")
        #         else:
        #             print(y, end=" , ")
        #             counter += 1
        #     print("]")
        # print("}")
        # return ''

    def __repr__(self):
        x= 'Graph: |V|='+ str(self.v_size()) + " |E|=" + str(self.e_size())
        return repr(x)


    # method used to compare between graphs by comparing all the nodes and the edges
    def __eq__(self, other):
        if len(self.get_all_v().values()) != len(other.get_all_v().values()):
            return False
        for node1, node2 in zip(self.get_all_v().values(), other.get_all_v().values()):
            if node1 != node2:
                return False
            if len(self.all_out_edges_of_node(node1.id)) != len(other.all_out_edges_of_node(node2.id)):
                return False
            for in1, in2 in zip(self.all_out_edges_of_node(node1.id).keys(), other.all_out_edges_of_node(node2.id).keys()):
                if in1 != in2:
                    return False
            if len(self.all_in_edges_of_node(node1.id)) != len(other.all_in_edges_of_node(node2.id)):
                return False
            for out1, out2 in zip(self.all_in_edges_of_node(node1.id).keys(), other.all_in_edges_of_node(node2.id).keys()):
                if out1 != out2:
                    return False

        return True


# this class represent a node in the graph
class Node:
    def __init__(self, key, pos):
        self.id = key
        self.tag = 0
        self.w = -1
        self.info = ''
        self.pos = pos
        self.ni_in = {}
        self.ni_out = {}

    # boolean method which return if an edge between to nodes exists or not
    def get_edge(self, id1):
        if self.ni_out.get(id1) is None:
            return False
        return True

    # method to compare between to nodes by the weight usefull in dijkstra algorithm
    def __lt__(self, other):
        return self.w < other.w

    # method to compare between to nodes by the weight usefull in dijkstra algorithm
    def __gt__(self, other):
        return self.w > other.w

    # method to compare between to nodes by the weight usefull in dijkstra algorithm
    def __eq__(self, other):
        return self.w == other.w

    # method to print a node by its key
    def __str__(self):
        print(self.id)
        return ''

    def __eq__(self, other):
        return self.id == other.id
