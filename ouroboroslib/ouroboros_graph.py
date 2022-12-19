from typing import Hashable, Any
from collections import namedtuple


class OuroborosGraph:
    """
    An adjacency list implementation of a Graph Abstract Data Type
    """

    class Edge:
        """
        An edge in an OuroborosGraph
        """

        __slots__ = "_start", "_end", "_data"

        def __init__(self, start: Any, end: Any, data: Any) -> None:
            """
            Initializes an edge
            :param start: start node of the edge
            :param end: end node of the edge
            :param data: data
            """
            self._start: Any = start
            self._end: Any = end
            self._data: Any = data

        def start(self) -> Any:
            """
            Returns the start node of the edge
            :return: start node of the edge
            """
            return self._start

        def end(self) -> Any:
            """
            Returns end node of the edge
            :return: end node of the edge
            """
            return self._end

        def data(self) -> Any:
            """
            Returns the data of the edge
            :return: data of the edge
            """
            return self._data

        def to_tuple(self) -> tuple:
            """
            Converts to a tuple
            :return: a tuple (start, end, data)
            """
            EdgeTuple = namedtuple('EdgeTuple', 'start end data')
            return EdgeTuple(start=self._start, end=self._end, data=self._data)

        def __hash__(self) -> int:
            return hash(id(self))

    def __init__(self, directed: bool = False) -> None:
        """
        Initializes an empty graph
        :param directed: whether the graph uses directed edges or not
        """
        self._size: int = 0
        self._num_edges: int = 0
        self._directed: bool = directed
        self._outgoing: dict = {}
        self._incoming: dict = {}

    def size(self) -> int:
        """
        Returns the number of nodes in the graph
        :return: number of nodes in the graph
        """
        return self._size

    def num_edges(self) -> int:
        """
        Returns the number of edges in the graph
        :return:
        """
        return self._num_edges

    def is_directed(self) -> bool:
        """
        Returns whether the graph is directed
        :return: True if the graph is directed, false otherwise
        """
        return self._directed

    def contains(self, x: Any) -> bool:
        """
        Returns whether node x exists in the graph
        :param x: The node to test
        :return: True if x is in the graph, false otherwise
        """
        return x in self._outgoing

    def contains_edge(self, x: Any, y: Any) -> bool:
        """
        Returns whether the edge (x, y) exists
        :param x: starting node of the edge
        :param y: ending node of the edge
        :return: True if the edge exists
        """
        return y in self._outgoing[x]

    def in_degree(self, x: Any) -> int:
        """
        Returns the indegree of node x
        :param x: the node to get an indegree of
        :return: the number of edges directed towards x
        """
        return len(self._incoming[x])

    def out_degree(self, x: Any) -> int:
        """
        Returns the outdegree of node x
        :param x: the node to get an outdegree of
        :return: the number of edges directed outward from x
        """
        return len(self._outgoing[x])

    def degree(self, x: Any) -> int:
        """
        Returns the sum of indegree and outdegree for x for a directed graph,
        Returns the number of edges incident to x for an undirected graph
        :param x: the node to get a degree of
        :return: the degree of x
        """
        if self.is_directed():
            return self.in_degree(x) + self.out_degree(x)
        return self.out_degree(x)

    def nodes(self) -> set[Any]:
        """
        Returns a set of all the nodes
        :return: A set of all the nodes
        """
        return set(self._outgoing.keys())

    def adjacent_nodes(self, x: Any) -> set[Any]:
        """
        Returns a set of the adjacent nodes to x, nodes
        which are immediately reachable by x
        :param x:
        :return: returns adjacent nodes
        """
        return set(self._outgoing[x].keys())

    def is_adjacent(self, x: Any, y: Any) -> bool:
        """
        Returns whether y is adjacent to x, which is True
        if y is immediately reachable by an edge from x
        :param x: the starting node
        :param y: the questioned node
        :return: True if y is adjacent to x, false otherwise
        """
        return y in self.adjacent_nodes(x)

    def edges(self) -> set[tuple]:
        """
        Returns a set of all the edges
        :return: A set of all the edges
        """
        def find_edges(mapping, result):
            for secondary_dict in mapping.values():
                result.update(secondary_dict.values())
        edges: set[OuroborosGraph.Edge] = set()
        find_edges(self._outgoing, edges)
        find_edges(self._incoming, edges)
        return {edge.to_tuple() for edge in edges}

    def add_node(self, x: Any) -> None:
        """
        Adds the node x to the graph
        :param x: the node to be added
        :return:
        :raises Exception: when node exists already
        :raises Exception: when node is not hashable
        """
        if not isinstance(x, Hashable):
            raise Exception("Node must be hashable.")
        if self.contains(x):
            raise Exception("Node exists already.")
        self._size += 1
        self._outgoing[x] = {}
        self._incoming[x] = {}

    def add_edge(self, x: Any, y: Any, value: Any = None) -> None:
        """
        Inserts an edge between x and y with data z
        :param x: the starting node of the edge
        :param y: the ending node of the edge
        :param value: data on the node
        :return:
        :raises Exception: when x or y are not nodes in the graph, or if edge exists
        """
        if not self.contains(x) or not self.contains(y):
            raise Exception("Cannot insert edge with missing node.")
        if self.contains_edge(x, y):
            raise Exception("Cannot insert edge that already exists.")
        if not isinstance(value, Hashable):
            raise Exception("Value on edge must be hashable.")
        self._num_edges += 1
        edge: OuroborosGraph.Edge = self.Edge(x, y, value)
        self._outgoing[x][y] = edge
        self._incoming[y][x] = edge
        if not self.is_directed():
            self._outgoing[y][x] = edge
            self._incoming[x][y] = edge

    def delete_node(self, x: Any) -> None:
        """
        Deletes the node from the graph and its associated edges
        :param x: the node to be deleted
        :return:
        :raises Exception: when x is not in the graph
        """
        if not self.contains(x):
            raise Exception("Cannot delete node that does not exist.")
        for y in self._outgoing[x]:
            del self._incoming[y][x]
        del self._outgoing[x]
        for y in self._incoming[x]:
            del self._outgoing[y][x]
        del self._incoming[x]
        self._size -= 1

    def delete_edge(self, x: Any, y: Any) -> None:
        """
        Deletes the edge from x to y. If graph is undirected, then
        deletes the undirected edge
        :param x: the starting node
        :param y: the ending node
        :return:
        :raises Exception: when nodes are missing
        :raises Exception: when edge does not exist
        """
        if not self.contains(x) or not self.contains(y):
            raise Exception("Cannot delete edge with missing node.")
        if not self.is_adjacent(x, y):
            raise Exception("Edge does not exist.")
        del self._outgoing[x][y]
        del self._incoming[y][x]
        if not self.is_directed():
            del self._outgoing[y][x]
            del self._incoming[x][y]
        self._num_edges -= 1

    def clear(self) -> None:
        """
        Resets the graph to an empty graph
        :return:
        """
        self._outgoing = {}
        self._incoming = {}
        self._num_edges = 0
        self._size = 0

    def overwrite_graph(self, node_list: list[Any] = [],
                        edge_list: list[tuple] = []) -> None:
        """
        Takes in a list of tuples (x, y, value) and overwrites the existing graph
        :param node_list: list of nodes to generate the new graph
        :param edge_list: list of edges to generate the new graph
        :return:
        """
        self.clear()
        for x in node_list:
            self.add_node(x)
        for x, y, value in edge_list:
            self.add_edge(x, y, value)
