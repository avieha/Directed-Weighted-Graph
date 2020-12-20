#                                                                    Directed Weighted Graph

 This project is divided to two parts. in the first part we implemnted a directed weighted graph, and in the second part 
 we use the directed weighted graph to tun a "pokemon" game

## Table of contents
* [General info](#general-info)
* [Data structure](#data-structure)
* [Algorithms](#algorithms)
* [Tests](#tests)
* [Launch](#launch)
* [Sources](#sources)

## General info

### Directed Wighted Graph:
a directed weighted graph(dwg) is a graph made from nodes - |V| and edges = |E| 
the classes which implemnt the dwg are int the folder "API" and they are:
* NodeData- this class implemnts the interface of "node_data" and it represent the nodes in the graph.
every node have a key, weight, info, tag and a location which is an inner class which implements the interface of "geo_location" wich represent a location of 3D.

* DWGraph_DS- this class represennt the graph and it has an inner class "EdgeData" which is the interface of "edge_data" and represent the edges whos connect the nodes
every edge have a positive weight, a source- the node the edge came from-, a destination- the node the edge go to-, info and tag.
in the DWGraph_DS you can find all the simple methods of the graph such as adding a node or an edge, reamoving a node or an edge, connecting nodes, get a list of the nodes 
or a list of all the neighboors of a specific node, and some more methods.

* DWGraph_Algo- this class allows you the make some manipulations over the graph. you can init a directed weighted graph graph run some functions like:
-copy- make a deep copy of the graph
-isconnected- check if the graph is strongly connected( you can go from every node to every node) using a BFs algorithm and the reversing alll the graph and run agaim the BfS from the same node
-shortestpathdist- return the shortest path (by the edges weight) between 2 nodes.
-shortestpath- return a list of nodes of the shortest path 
-save- save a file of the graph in a Json form.. in this method we used the GSon library of google
-load- load a saved Json file and create anew graph.  in this method we used the GSon library of google

### pokemon game
In the pokemon game the player enters his own id and a level number, which sent to the server, and than the game runs totally automated, with smart planned algorithm which knows where to send the agents at each round, when every agent can go to his neighbors only.
after each pokemon is being eaten, a new one is being immidiatley generting, at the end the best Score determined by value of eaten pokemons, and a limit of 10 'moves' per second.

## Data Structure
We decide to write this project using 3 Hasmaps. 1 for the nodes and 2 for the edges. the first hasmap of the edges is used to keep all the edges that come out
from every node in the graph
and the third hashmap is to keep for every node the edges the came to him. The reson we needed 2 hashamp for the edges is that you need to know for every node 
to which nodes is connected and which nodes are connected to him. In that way when you remov a node you acan also remove all the edges which were connected to
him and all the nodes he were connected to. the others reasons we used hashmap are becuase it allows you to get every node in o(1), it allows you to contain many nodes without initialize a a size at first,
and beacuase it also have the function value which let you convert the hasmap into a list with just a pointer in o(1)

## Algorithms
* Kosaraju's- We used it at the method isConnected, the algorithm run over the graph with a bfs traversal, reverse the graph, and then starts another BFS from the same node. 
if all nodes were visited the graph is storngly connected.
Time complexity of above implementation is same as Breadth First Search which is O(V+E).

* Dijikstra- we used it in the shortestpath methods(both path and distance), the algortihm used a PriorityQueue with a comparator(by weight), and finds the shortest path/distance(more info on the project's wiki).
  
## Tests
in the folder "tests" you can find 3 Junit classes that test all the methods in the DWGraph_Algo and all the methods in DWGraph_DS,the tests checks simple methods like adding or removing a node to the complex methods like isconnected or shortestpath, there is also another test that checks the logic methods in Ex2, init and nextNodedist.

## Launch
To run this project you need at first to Pull the file from the Git repository with the command :
```
$ git clone https://github.com/avieha/ex2.git 
```
then you have several options
1) run the ex2.jar file by double clicking on it.

2) from CMD: open your terminal and insert those commands:
```
$ java -jar ex2 <id number> <game level>
```
(you can choose levels between 0-23)
		
3) from your java Development Environment.
you need to run the main program which is EX2
after running the main you will see the login window there you will have to insert your id and the game level ([0,23])
and the game will start.

## Sources
In the algorithm of Dijikstra i get help from a youtube video: https://www.youtube.com/watch?v=FSm1zybd0Tk 

info about Kosaraju's algorithm https://en.wikipedia.org/wiki/Strongly_connected_component
https://www.geeksforgeeks.org/check-given-directed-graph-strongly-connected-set-2-kosaraju-using-bfs/?ref=rp

```