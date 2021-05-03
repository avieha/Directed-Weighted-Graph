#                                                                    Directed Weighted Graph

 In this project we implemented a Directed Weighted Graph using pytho 3.8

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
the classes which implemnt the dwg are int the folder "pack" and they are:
* Digraph- this class represent the graph. it has an inner class named "node" wich represent the nodes in the graph.
every node have the next values: id,info,pos(3d position),tag and w(which helps in algoritms)and 2 dictionaries to keep for every node 
  its edgdes which go out from it and the edges came in from other nodes. We dont used a class for the edge and insted we just represant the edges using the nodes, like we said every nodes stores its neighboors.
  In the class Digraph we have a dictionary to keep all the nodes in the graph and a value to store the edges number and a value mc which idicates the number of changes the graph made(like removeing a node or adding an edge)
  In this class you can find all the simple methods of the graph such as adding a node or an edge, reamoving a node or an edge, connecting nodes, get a list of the nodes 
or a list of all the neighboors of a specific node, and some more methods.

* GraphAlgo- this class allows you the make some manipulations over the graph. you can init a directed weighted graph,and run some functions like:
-isconnected- check if the graph is strongly connected( you can go from every node to every node) using a BFs algorithm and the reversing alll the graph and run agaim the BfS from the same node
-shortestpath- return the shortest path (by the edges weight) between 2 nodes and the list of nodes of the shortest path 
-save- save a file of the graph in a Json form
-load- load a saved Json file and create anew graph.
-connected component- this method return the biggest strongly connected component of a given node.
-connected components- this method return a list of lists of all the strongly connected components in the graph
-plot_graph-this method show an image of the graph. in this method we used the library Matplotlb
  
## Data Structure
We decide to write this project using 2 dictionaries for every node. those dictionaries store all the edges which come in from every node and go out to every neighbor
besides thos dictinaries we have another dictionary wich store all the nodes in the graph.
the reasons we used dictionaries are because:
1) in dictionary you dont have doplicates keys, this helps to avoid 2 nodes with same key.

2)  in the dictionary you can reach every node with just O(1) thats allows us to delete nodes and edges or to add nodes and edges fastly and easily. 

## Algorithms
* connected component/s- "naive algorithm"- in the naive algorithm you run a DFS over the graph starting from one node then you traspose
the graph and run again a DFS from the same node after that the visited nodes in both of the DFS are the strongly connected componnent(scc).
  to reach all the connected componnents in the graph we call the connected componnent and marked every node which is part of the 
  component we recived this way helps you to avoid getting the same scc twice or even more.

* Dijikstra- we used it in the shortestpath methods(both path and distance), the algortihm used a PriorityQueue with a comparator(by weight), and finds the shortest path/distance(more info on the project's wiki).
  
## Tests
in the folder "tests" you can find 2 unit test classes that test all the methods in the GraphAlgo and all the methods in Digraph,the tests checks simple methods like adding or removing a node to the complex methods like connected components or shortestpath.


## Launch
To run this project you need at first to Pull the file from the Git repository with the command :
```
$ git clone https://github.com/avieha/Directed-Weighted-Graph.git 
```
then you can open the project in your ide, make a main class and start to use it ( maybe you will need to download the metplotlib
library. you can do it be pressing with the right button of the mouse on the "matplotlib" from the "import matplotlib" in  start of the AlgoGraph class)

## Sources
In the algorithm of Dijikstra i get help from a youtube video: https://www.youtube.com/watch?v=FSm1zybd0Tk 

In the plot_graph i get helpfrom  the examples in matlpotlib web site: https://matplotlib.org/gallery/index.html 



```
