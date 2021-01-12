import unittest
from unittest import TestCase
from pack.GraphAlgo import GraphAlgo
from pack.DiGraph import DiGraph
import json

if __name__ == '__main__':
    unittest.main()


class TestGraphAlgo(TestCase):

    def test_get_graph(self):

        graph = DiGraph()
        graph.add_node(1)
        g = GraphAlgo(graph)
        self.assertEqual(len(g.get_graph().get_all_v()), 1)

    def test_load_from_json(self):
        g = GraphAlgo()
        self.assertFalse(g.load_from_json("not existed graph"))
        g.load_from_json('../data/A0')
        i = 0
        for node in g.get_graph().get_all_v().values():
            self.assertEqual(i, node.id)
            i = i + 1
        list = [1, 10]  # node out from 0 and node in from 0
        i = 0
        for node in g.get_graph().all_in_edges_of_node(0).values():
            self.assertEqual(list[i], node.id)
            i = i + 1
        i = 0
        for node in g.get_graph().all_out_edges_of_node(0).values():
            self.assertEqual(list[i], node[0].id)
            i = i + 1

    def test_save_to_json(self):
        g = GraphAlgo()
        g.load_from_json('../data/A0')
        g.save_to_json('save_test')
        graph = GraphAlgo()
        graph.load_from_json('save_test')
        self.assertEqual(g.get_graph(), graph.get_graph())

    def test_shortest_path(self):
        g = DiGraph()
        for i in range(7):
            g.add_node(i)
        g.add_edge(0, 1, 5)
        g.add_edge(0, 2, 3)
        g.add_edge(0, 1, 5)
        g.add_edge(1, 6, 12.1)
        g.add_edge(2, 3, 2)
        g.add_edge(2, 5, 8)
        g.add_edge(3, 4, 1)
        g.add_edge(4, 5, 4)
        g.add_edge(5, 6, 7)
        graph = GraphAlgo(g)
        self.assertTupleEqual(graph.shortest_path(0, 6), (17, [0, 2, 3, 4, 5, 6]))
        graph.g.add_edge(1, 6, 11.9)
        self.assertTupleEqual(graph.shortest_path(0, 6), (16.9, [0, 1, 6]))
        self.assertTupleEqual(graph.shortest_path(6, 0), (float('inf'), []))
        self.assertTupleEqual(graph.shortest_path(0, 9), (float('inf'), []))
        self.assertTupleEqual(graph.shortest_path(0, 0), (0, [0]))

    def test_connected_component(self):
        g = DiGraph()
        for i in range(7):
            g.add_node(i)
        g.add_edge(0, 1, 5)
        g.add_edge(0, 2, 3)
        g.add_edge(0, 1, 5)
        g.add_edge(1, 6, 12.1)
        g.add_edge(2, 3, 2)
        g.add_edge(2, 5, 8)
        g.add_edge(3, 4, 1)
        g.add_edge(4, 5, 4)
        g.add_edge(5, 6, 7)
        g.add_edge(3, 0, 1)
        g.add_edge(1, 3, 5)
        graph = GraphAlgo(g)
        self.assertListEqual(graph.connected_component(0), [0, 1, 2, 3])
        g.remove_edge(1, 3)
        self.assertListEqual(graph.connected_component(0), [0, 2, 3])
        g.add_edge(5, 0, 8)
        self.assertListEqual(graph.connected_component(0), [0, 2, 3, 4, 5])

    def test_reverse_graph(self):
        g = DiGraph()
        graph = DiGraph()
        for i in range(5):
            g.add_node(i)
            graph.add_node(i)
        g.add_edge(1, 2, 3)
        graph.add_edge(2, 1, 3)
        g.add_edge(0, 4, 3)
        graph.add_edge(4, 0, 3)
        g.add_edge(1, 3, 3)
        graph.add_edge(3, 1, 3)
        g.add_edge(3, 2, 3)
        graph.add_edge(2, 3, 3)
        algo = GraphAlgo(g)
        self.assertNotEqual(algo.g, graph)
        algo.g = algo.reverse_graph(algo.get_graph())
        self.assertEqual(graph, algo.get_graph())

    def test_connected_components(self):
        g = DiGraph()
        for i in range(7):
            g.add_node(i)
        g.add_edge(0, 1, 5)
        g.add_edge(0, 2, 3)
        g.add_edge(0, 1, 5)
        g.add_edge(1, 6, 12.1)
        g.add_edge(2, 3, 2)
        g.add_edge(2, 5, 8)
        g.add_edge(3, 4, 1)
        g.add_edge(4, 5, 4)
        g.add_edge(5, 6, 7)
        g.add_edge(6, 5, 4)
        g.add_edge(3, 0, 1)
        g.add_edge(1, 3, 5)
        graph = GraphAlgo(g)
        self.assertEqual(graph.connected_components(), [[0, 1, 2, 3], [4], [5, 6]])
        graph.g.remove_edge(1, 3)
        self.assertEqual(graph.connected_components(), [[0, 2, 3], [1], [4], [5, 6]])
        graph.get_graph().remove_node(0)
        self.assertEqual(graph.connected_components(), [[1], [2], [3], [4], [5, 6]])
