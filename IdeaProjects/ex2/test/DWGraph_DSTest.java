package tests;

import api.*;
import org.junit.jupiter.api.Test;

import java.util.Collection;
import java.util.Iterator;

import static org.junit.jupiter.api.Assertions.*;

class DWGraph_DSTest {
    /**
     * checking normal node and null node
     */
    @Test
    void getNode() {
        directed_weighted_graph g = new DWGraph_DS();
        node_data x= new NodeData(5);
        node_data y= new NodeData(5);
        node_data z= new NodeData(7);
        g.addNode(x);
        g.addNode(y);
        g.addNode(z);
        node_data s=g.getNode(5);
        node_data t=g.getNode(10);
        assertEquals(5,s.getKey());
        assertNull(t);
    }
    /**
     * checking edge's weight of connected nodes, not connected nodes and doesnt exists nodes.
     * and checking edge info
     */

    @Test
    void getEdge() {
        directed_weighted_graph g = new DWGraph_DS();
        node_data one= new NodeData(1);
        node_data two= new NodeData(2);
        node_data thr= new NodeData(3);
        node_data four= new NodeData(4);
        node_data five= new NodeData(5);

        g.addNode(one);
        g.addNode(two);
        g.addNode(thr);
        g.addNode(four);
        g.addNode(five);
        g.connect(1,2,0.6);
        g.connect(1,3,4.2);
        g.connect(4,2,2.1);
        g.connect(4,3,45.9);
        g.connect(5,5,5);
        edge_data x=g.getEdge(1,2);
        edge_data y=g.getEdge(2,2);
        edge_data z=g.getEdge(8,2);
        edge_data t=g.getEdge(1,5);
        x.setInfo("holaa");
        assertEquals(0.6,x.getWeight());
        assertNull(y);
        assertNull(z);
        assertNull(t);
        assertEquals(g.getNode(one.getKey()).getKey(),g.getEdge(1,2).getSrc());
        assertEquals(two.getKey(),g.getEdge(1,2).getDest());
        assertEquals("holaa",g.getEdge(1,2).getInfo());
    }
    /**
     * checking node size after adding the same node
     */
    @Test
    void addNode() {
        directed_weighted_graph g = new DWGraph_DS();
        node_data one= new NodeData(1);
        node_data two= new NodeData(2);
        node_data thr= new NodeData(1);

        g.addNode(one);
        g.addNode(two);
        g.addNode(thr);
        int x=g.nodeSize();
        assertEquals(2,x);
    }
    /**
     * checking the connect method between normal nodes ,doesnt exists nodes,same node,negative weight
     * and after setting weight again
     */
    @Test
    void connect() {
        directed_weighted_graph g = new DWGraph_DS();
        node_data one= new NodeData(1);
        node_data two= new NodeData(2);
        node_data thr= new NodeData(3);
        node_data four= new NodeData(4);
        node_data five= new NodeData(5);
        g.addNode(one);
        g.addNode(two);
        g.addNode(thr);
        g.addNode(four);
        g.addNode(five);
        g.connect(1,2,0.6);
        g.connect(1,3,-4.2);
        g.connect(4,6,2.1);
        g.connect(4,5,45.9);
        g.connect(5,4,5);
        g.connect(5,5,5);
        edge_data x=g.getEdge(5,5);
        assertNull(x);
        assertNull(g.getEdge(1,3));
        assertNull(g.getEdge(4,6));
        assertEquals(0.6,g.getEdge(1,2).getWeight());
        assertEquals(45.9,g.getEdge(4,5).getWeight());
    }
    /**
     * checking the nodes of the graph are not null and that the collection have the same size of
     * nodesize
     */
    @Test
    void getV() {
        directed_weighted_graph g = new DWGraph_DS();
        node_data one= new NodeData(1);
        node_data two= new NodeData(2);
        node_data thr= new NodeData(3);
        node_data four= new NodeData(4);
        node_data five= new NodeData(5);
        g.addNode(one);
        g.addNode(two);
        g.addNode(thr);
        g.addNode(four);
        Collection<node_data> v = g.getV();
        Iterator<node_data> iter = v.iterator();
        while (iter.hasNext()) {
            node_data n = iter.next();
            assertNotNull(n);
        }
        assertEquals(g.nodeSize(),v.size());
    }
    /**
     * checking the neighbors of real node are not null and the neighbors of
     * not real node are null
     */
    @Test
    void getE() {
        directed_weighted_graph g = new DWGraph_DS();
        node_data one= new NodeData(1);
        node_data two= new NodeData(2);
        node_data thr= new NodeData(3);
        node_data four= new NodeData(4);
        node_data five= new NodeData(5);
        g.addNode(one);
        g.addNode(two);
        g.addNode(thr);
        g.addNode(four);
        g.addNode(five);
        g.connect(1,2,1);
        g.connect(1,3,2);
        g.connect(2,3,3);
        g.connect(3,1,1);
        Collection<edge_data> v = g.getE(1);
        Iterator<edge_data> iter = v.iterator();
        int index=1;
        while (iter.hasNext()) {
            edge_data n = iter.next();
            assertEquals(index++,n.getWeight());
            assertEquals(index,n.getDest());
        }
        Collection<edge_data> t = g.getE(6);
        assertNull(t);
    }
    /**
     * checking the nullity of a removed node and a doesnt exists node
     * and that all the edges which were connected to removed node
     * have been removed
     * checking edgesize and nodesize
     */
    @Test
    void removeNode() {
        directed_weighted_graph g = new DWGraph_DS();
        node_data one= new NodeData(1);
        node_data two= new NodeData(2);
        node_data thr= new NodeData(3);
        g.addNode(one);
        g.addNode(two);
        g.addNode(thr);
        g.connect(1,2,5);
        g.connect(3,1,5);
        node_data x = g.removeNode(1);
        node_data y=  g.removeNode(1);
        node_data z=g.removeNode(8);
        assertNull(g.getNode(1));
        assertNull(y);
        assertNull(z);
        assertNull(g.getEdge(1,2));
        assertNull(g.getEdge(3,1));
        assertEquals(0,g.edgeSize());
        assertEquals(2,g.nodeSize());

    }
    /**
     *  simple remove edge method
     */
    @Test
    void removeEdge() {
        directed_weighted_graph g = new DWGraph_DS();
        node_data one= new NodeData(1);
        node_data two= new NodeData(2);
        node_data thr= new NodeData(3);
        g.addNode(one);
        g.addNode(two);
        g.addNode(thr);
        g.connect(1,2,8);
        assertNull(g.removeEdge(2,1));
        assertEquals(8,g.removeEdge(1,2).getWeight());

    }
    /**
     * checking the node size after adding nodes and after removing the same node twice. removing a dosent exist node
     * and removing a regular node
     */
    @Test
    void nodeSize() {
        directed_weighted_graph g = new DWGraph_DS();
        node_data one= new NodeData(1);
        node_data two= new NodeData(2);
        node_data thr= new NodeData(3);
        node_data four= new NodeData(4);
        node_data five= new NodeData(5);
        g.addNode(one);
        g.addNode(two);
        g.addNode(thr);
        g.addNode(four);
        g.addNode(five);
        assertEquals(5,5);
        g.removeNode(5);
        g.removeNode(5);
        g.removeNode(1);
        g.removeNode(8);
        assertEquals(3,3);

    }
    /**
     * checking the edge size after connecting nodes
     * after connecting node to himself
     * after connecting not existing node
     * after connecting same nodes with a diff weight and with same weight
     * and after removing node
     */
    @Test
    void edgeSize() {
        directed_weighted_graph g = new DWGraph_DS();
        node_data one= new NodeData(1);
        node_data two= new NodeData(2);
        node_data thr= new NodeData(3);
        node_data four= new NodeData(4);
        node_data five= new NodeData(5);
        g.addNode(one);
        g.addNode(two);
        g.addNode(thr);
        g.addNode(four);
        g.addNode(five);
        g.connect(1,2,1);
        g.connect(2,2,2);
        g.connect(2,1,3);
        assertEquals(2,g.edgeSize());
        g.connect(2,1,3);
        g.connect(2,1,5);
        g.connect(1,3,1);
        g.connect(4,5,2);
        g.connect(3,2,1);
        assertEquals(5,g.edgeSize());
        g.removeEdge(2,1);
        g.removeNode(3);
        assertEquals(2,g.edgeSize());
    }

}