# Ouroboroslib

A library of graph theory algorithms. Named after the symbol of a serpent eating its own tail. The Ouroboros Graph
implements an adjacency list data structure for its underlying graph representation.

## Installation

`pip3 install ouroboroslib`

Library requires Python 3.9.0 or higher.

## Usage

```py
from ouroboroslib import OuroborosGraph

ouroboros = OuroborosGraph(directed=True)
ouroboros.overwrite_graph(edge_list=[(1, 2, 7), (2, 3, 10)])
ouroboros.add_node(4)
ouroboros.add_edge(3, 4, value=7)
ouroboros.delete_node(2)
edges = ouroboros.edges()
x, y, value = edges.pop() # x = 3, y = 4, value = 7
```
