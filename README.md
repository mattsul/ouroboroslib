# Ouroboroslib  
  
A library of graph theory algorithms. Named after the symbol of a serpent eating its own tail. The Ouroboros Graph  
implements an adjacency list data structure for its underlying graph representation.  
  
## Installation  
  
`pip3 install ouroboroslib`  
  
Library requires Python 3.9.0 or higher.  
  
## Example Usage  
  
```py  
from ouroboroslib import OuroborosGraph  
  
ouroboros = OuroborosGraph(directed=True)  
ouroboros.overwrite_graph(
	node_list=[1, 2, 3],
	edge_list=[(1, 2, 7), (2, 3, 10)])  
ouroboros.add_node(4)  
ouroboros.add_edge(3, 4, value=7)  
ouroboros.delete_node(2)  
for x, y, value in ouroboros.edges():
	assert ouroboros.is_adjacent(x, y)  
```  

## Features  

* Supports undirected and directed graphs.
* Supports any data type for nodes as long as it is hashable.
* Supports attaching a value to the edges as long as it is hashable.
* Supports the basic operations of a graph abstract data type.
	* `OuroborosGraph.size()`: Returns the number of nodes in the graph.
	* `OuroborosGraph.num_edges()`: Returns the number of edges in the graph.
	* `OuroborosGraph.is_directed()`: Returns whether the graph is directed or not.
	* `OuroborosGraph.contains(x)`: Returns whether `x` is a node in the graph.
	* `OuroborosGraph.contains_edge(x, y)`: Returns whether the edge `(x, y)` exists in the graph.
	* `OuroborosGraph.in_degree(x)`: Returns the number of edges incoming to `x`.
	* `OuroborosGraph.out_degree(x)`: Returns the number of edges outgoing from `x`.
	* `OuroborosGraph.degree(x)`: Returns the number of incoming and outgoing edges incident to `x`.
	* `OuroborosGraph.nodes()`: Returns a set of all the nodes in the graph.
	* `OuroborosGraph.adjacent_nodes(x)`: Returns a set of all the nodes incident to edges outgoing `x`.
	* `OuroborosGraph.is_adjacent(x, y)`: Returns whether `y` is incident to an edge outgoing `x`.
	* `OuroborosGraph.edges()`: Returns a set of all the edges in the graph.
	* `OuroborosGraph.add_node(x)`: Adds the node `x` to the graph.
	* `OuroborosGraph.add_edge(x, y, value)`: Adds the edge `(x, y)` with edge data `value`.
	* `OuroborosGraph.delete_node(x)`: Deletes the node `x` from the graph.
	* `OuroborosGraph.delete_edge(x, y)`: Deletes the edge `(x, y)` from the graph.
	* `OuroborosGraph.clear()`: Resets the graph to an empty graph.
	* `OuroborosGraph.overwrite_graph(node_list, edge_list)`: Initializes the graph with `node_list` and `edge_list`.

## Contributing

Please feel free to open up pull requests! There is so much to graph theory 
and graph algorithms that I don't know yet, so contributions (whether bug fixes or features) are 
very much appreciated!