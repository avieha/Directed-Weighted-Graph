package tests;

import api.*;
import org.junit.jupiter.api.Test;

import java.util.Iterator;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class DWGraph_AlgoTest {
    /**
     * test checking 2 copy graph are deeply copied by equalizing the graph at first and after changes
     */
    @Test
    void copy() {
        directed_weighted_graph g=small_graph();
        dw_graph_algorithms ag0 = new DWGraph_Algo();
        ag0.init(g);
        directed_weighted_graph g2= ag0.copy();
        assertEquals(g,g2);
        assertEquals(g.edgeSize(),g2.edgeSize());
        assertEquals(g.nodeSize(),g2.nodeSize());
        g2.removeNode(5);
        assertNotEquals(g.edgeSize(),g2.edgeSize());
        assertNotEquals(g.nodeSize(),g2.nodeSize());
        g2.getNode(1).setTag(100);
        g2.getNode(1).setInfo("checking");
        assertNotEquals(g.getNode(1).getTag(),g2.getNode(1).getTag());
        assertNotEquals(g.getNode(1).getInfo(),g2.getNode(1).getInfo());
    }
    /**
     * testing connectivity in a connected graph and not connected graph
     */
    @Test
    void isConnected() {
        directed_weighted_graph g=small_graph();
        dw_graph_algorithms ag0 = new DWGraph_Algo();
        ag0.init(g);
        assertTrue(ag0.isConnected());
        node_data n=new NodeData(15);
        g.addNode(n);
        assertFalse(ag0.isConnected());
        g.connect(15,8,8);
        g.removeNode(5);
        g.removeNode(7);
        assertFalse(ag0.isConnected());
    }
    /**
     * testing the shortest path distanece between two node, between same node between not connected nodes
     * between not existing nodes and after setting new weight
     */
    @Test
    void shortestPathDist() {
        directed_weighted_graph g=small_graph();
        dw_graph_algorithms ag0 = new DWGraph_Algo();
        ag0.init(g);
        g.connect(8,1,20);
        g.connect(6,7,15);
        assertEquals(-1,ag0.shortestPathDist(3,56));
        assertEquals(27,ag0.shortestPathDist(3,1));
        assertEquals(23,ag0.shortestPathDist(1,7));
        assertEquals(0,ag0.shortestPathDist(3,3));
        g.removeNode(5);
        g.removeNode(6);
        g.removeNode(7);
        g.removeNode(8);
        assertEquals(-1,ag0.shortestPathDist(1,3));
        assertEquals(2,ag0.shortestPathDist(1,2));
        assertEquals(1,ag0.shortestPathDist(3,4));
    }

    /**
     * checking the path between nodes, between not connected node and between not existing nodes
     */
    @Test
    void shortestPath() {
        directed_weighted_graph g=small_graph();
        dw_graph_algorithms ag0 = new DWGraph_Algo();
        ag0.init(g);
        node_data n=new NodeData(50);
        g.addNode(n);
        List<node_data> sp = ag0.shortestPath(1,7);
        List<node_data> sp2 = ag0.shortestPath(1,50);
        List<node_data> sp3 = ag0.shortestPath(1,27);
        List t= ag0.shortestPath(1,7);
        double []x=new double [t.size()];
        double []y={1,2,6,3,4,7};
        int i=0;
        Iterator<node_data> it=t.iterator();
        while (it.hasNext()){
            x[i++]=it.next().getKey();
        }
        assertArrayEquals(x,y);
        assertNull(sp2);
        assertNull(sp3);
    }

    /**
     * this test save a graph and after it load the ssaved graph to a new graph and check if they are an equal deep copy
     */
    @Test
    void save_load() {
        directed_weighted_graph g0 = small_graph();
        dw_graph_algorithms ag0 = new DWGraph_Algo();
        dw_graph_algorithms ag2 = new DWGraph_Algo();
        ag0.init(g0);
        String str = "save_load_test.obj";
        ag0.save(str);
        ag2.load(str);
        directed_weighted_graph g2 = ag2.getGraph();
        assertEquals(g0,g2);
        g0.removeNode(1);
        assertNotEquals(g0,g2);
    }

    private directed_weighted_graph small_graph() {
        directed_weighted_graph g = new DWGraph_DS();
        node_data one= new NodeData(1);
        node_data two= new NodeData(2);
        node_data thr= new NodeData(3);
        node_data four= new NodeData(4);
        node_data five= new NodeData(5);
        node_data six= new NodeData(6);
        node_data seven= new NodeData(7);
        node_data eight= new NodeData(8);


        g.addNode(one);
        g.addNode(two);
        g.addNode(thr);
        g.addNode(four);
        g.addNode(five);
        g.addNode(six);
        g.addNode(seven);
        g.addNode(eight);

        g.connect(1,2,2);
        g.connect(2,6,7);
        g.connect(6,3,4);
        g.connect(3,4,1);
        g.connect(4,7,9);
        g.connect(7,8,5);
        g.connect(8,5,4);
        g.connect(5,6,7);
        g.connect(5,4,13);
        g.connect(5,1,8);



        return g;
    }
}