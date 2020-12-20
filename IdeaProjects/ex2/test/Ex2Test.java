package tests;

import Server.Game_Server_Ex2;
import api.*;
import gameClient.Arena;
import gameClient.CL_Agent;
import gameClient.Ex2;

import org.junit.jupiter.api.Order;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestMethodOrder;
import org.junit.jupiter.api.MethodOrderer.OrderAnnotation;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Iterator;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

@TestMethodOrder(OrderAnnotation.class)
class Ex2Test {


    @Test
    @Order(1)
    void nextNodedist() {
        game_service game = Game_Server_Ex2.getServer(10);
        Ex2 a=new Ex2();
        directed_weighted_graph gg = initgame(game,a);
        assertEquals(a.nextNodedist(game, gg, 0, 9), 23);
    }

    @Test
    @Order(2)
    void init() {
        game_service game = Game_Server_Ex2.getServer(23);
        Ex2 a=new Ex2();
        directed_weighted_graph gg = initgame(game,a);
        List<CL_Agent> ag = Arena.getAgents(game.getAgents(), gg);
        Iterator<CL_Agent> it = ag.iterator();
        assertEquals(it.next().getSrcNode(), 38);
        assertEquals(it.next().getSrcNode(), 19);
        assertEquals(it.next().getSrcNode(), 12);
    }

    public directed_weighted_graph initgame(game_service game, Ex2 x) {
        String g = game.getGraph();
        try {
            PrintWriter pw = new PrintWriter(new File("graph.txt"));
            pw.write(g);
            pw.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        dw_graph_algorithms g0 = new DWGraph_Algo();
        g0.load("graph.txt");
        directed_weighted_graph gg = g0.getGraph();
        x.init(game, gg);
        return gg;
    }
}