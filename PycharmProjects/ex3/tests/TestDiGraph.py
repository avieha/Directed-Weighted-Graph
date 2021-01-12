import unittest
from unittest import TestCase
from pack import *
from pack.DiGraph import DiGraph

if __name__ == '__main__':
    unittest.main()


class TestDiGraph(TestCase):
    def test_v_size(self):
        g = DiGraph()
        for i in range(7):
            g.add_node(i)
        g.add_node(0)
        g.add_node(2)
        g.remove_node(3)
        g.remove_node(3)
        g.remove_node(4)
        self.assertEqual(g.v_size(), 5)

    def test_e_size(self):
        g = DiGraph()
        for i in range(7):
            g.add_node(i)
        g.add_edge(1,1,3)
        g.add_edge(1,2,4)
        g.add_edge(1, 6, -8)
        g.add_edge(2,1,7)
        g.add_edge(2,1,7)
        g.add_edge(5, 2, 4)
        g.add_edge(32, 45, 4)
        g.add_edge(1, 9, 4)
        g.add_edge(1,2,3)
        self.assertEqual(g.e_size(),3)

    def test_get_all_v(self):
        g = DiGraph()
        for i in range(7):
            g.add_node(i)
        dict = g.get_all_v()
        self.assertEqual(len(dict),7)
        g.remove_node(6)
        dict = g.get_all_v()
        for i in range(6):
            self.assertEqual(dict[i].id, i)

    def test_all_in_edges_of_node(self):
        g = DiGraph()
        for i in range(7):
            g.add_node(i)
        g.add_edge(1, 1, 3)
        g.add_edge(1, 2, 4)
        g.add_edge(1, 6, -8)
        g.add_edge(2, 1, 7)
        g.add_edge(2, 1, 7)
        g.add_edge(4, 1, 4)
        g.add_edge(32, 1, 4)
        g.add_edge(5, 1, 4)
        g.add_edge(5, 1, 3)
        g.add_edge(3, 1, 3)
        g.remove_node(3)
        g.add_edge(6, 1, 3)
        g.remove_edge(6, 1)
        self.assertIsNone(g.all_in_edges_of_node(22), None)
        dict = g.all_in_edges_of_node(1)
        self.assertEqual(len(dict),3)


    def test_all_out_edges_of_node(self):
        g = DiGraph()
        for i in range(7):
            g.add_node(i)
        g.add_edge(1, 1, 3)
        g.add_edge(1, 2, 4)
        g.add_edge(1, 6, -8)
        g.add_edge(1, 2, 7)
        g.add_edge(1, 3, 7)
        g.add_edge(1, 4, 4)
        g.add_edge(1, 18, 4)
        g.remove_node(3)
        g.add_edge(1, 6, 3)
        g.remove_edge(1, 6)
        g.add_edge(1, 5, 3)
        self.assertIsNone(g.all_out_edges_of_node(22), None)
        dict = g.all_out_edges_of_node(1)
        list = []
        for key in dict.values():
            list.append(key[0].id)
        sec_list=[2,4,5]
        self.assertListEqual(list,sec_list)

    def test_get_mc(self):
        g = DiGraph()
        for i in range(7):
            g.add_node(i)
        g.add_edge(1, 1, 3)
        g.add_edge(1, 2, 4)
        g.add_edge(1, 6, -8)
        g.add_edge(2, 1, 7)
        g.add_edge(2, 1, 7)
        g.add_edge(4, 1, 4)
        g.add_edge(32, 1, 4)
        g.add_edge(5, 1, 4)
        g.add_edge(5, 1, 3)
        g.add_edge(3, 1, 3)
        g.remove_node(3)
        g.add_edge(6, 1, 3)
        g.remove_edge(6, 1)
        self.assertEqual(g.get_mc(),16)

    def test_add_edge(self):
        g = DiGraph()
        for i in range(7):
            g.add_node(i)
        g.add_edge(1,2,3)
        g.add_edge(1, 2, 3)
        g.add_edge(1, 2, 4)
        self.assertFalse(g.add_edge(1, 87, 3))
        g.add_edge(92, 2, 3)
        self.assertFalse(g.add_edge(1, 5, -3))
        self.assertFalse(g.add_edge(1, 1, 3))
        g.add_edge(4, 5, 3)
        self.assertEqual(g.e_size(),2)



    def test_get_node(self):
        g = DiGraph()
        for i in range(7):
            g.add_node(i)
        self.assertIsNone(g.get_node(8))
        g.remove_node(5)
        self.assertIsNone(g.get_node(5))
        list=[0,1,2,3,4,6]
        sec_list = []
        for key in g.get_all_v().values():
            sec_list.append(g.get_node(key.id).id)
        self.assertListEqual(list,sec_list)



    def test_add_node(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(1)
        g.add_node(2)
        self.assertEqual(2, len(g.get_all_v()))

    def test_remove_node(self):
        g = DiGraph()
        for i in range(7):
            g.add_node(i)
        self.assertFalse(g.remove_node(14))
        self.assertTrue(g.remove_node(5))
        self.assertFalse(g.remove_node(5))
        self.assertTrue(g.remove_node(3))
        self.assertEqual(len(g.get_all_v()),5)


    def test_get_edge(self):
        g = DiGraph()
        for i in range(7):
            g.add_node(i)
        g.add_edge(1, 1, 3)
        g.add_edge(1, 2, 4)
        g.add_edge(1, 6, -8)
        g.add_edge(2, 1, 7)
        g.add_edge(2, 1, 9)
        g.add_edge(4, 1, 4)
        g.add_edge(32, 1, 4)
        g.add_edge(5, 1, 4)
        g.add_edge(5, 1, 3)
        g.add_edge(3, 1, 3)
        g.remove_node(3)
        g.add_edge(6, 1, 3)
        g.remove_edge(6, 1)
        self.assertIsNone(g.get_edge(6,1))
        self.assertIsNone(g.get_edge(6, 6))
        self.assertIsNone(g.get_edge(4,5 ))
        self.assertIsNone(g.get_edge(3, 9))
        self.assertEqual(g.get_edge(1,2),4)
        self.assertEqual(g.get_edge(2, 1), 7)


    def test_remove_edge(self):
        g = DiGraph()
        for i in range(7):
            g.add_node(i)
        for i in range(4):
            g.add_edge(i,i+1,5)
        self.assertFalse(g.remove_edge(1,6))
        self.assertFalse(g.remove_edge(7, 6))
        g.add_edge(0,2,2)
        g.add_edge(0, 3, 2)
        g.add_edge(0, 4, 2)
        g.add_edge(0, 5, 2)
        g.remove_edge(0,1)
        g.remove_edge(0, 4)
        list = [2,3,5]
        sec_list=[]
        for key in g.all_out_edges_of_node(0).values():
            sec_list.append(key[0].id)
        self.assertListEqual(sec_list, list)