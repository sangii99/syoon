from graph_library import *
import heapq
from functools import total_ordering

@total_ordering
class SpecialSorted:

    def __init__(self, element, value):
        self.element = element
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

class PriorityQueue:

    def __init__(self, sortkey = lambda x : x):
        self.content = []
        self.sortkey = sortkey

    def add(self, item):
        heapq.heappush(self.content, SpecialSorted(item, self.sortkey(item)))

    def peek(self):
        return self.content[0].element if self.content else None

    def poll(self):
        return heapq.heappop(self.content).element if len(self.content) > 0 else None

    def is_empty(self):
        return len(self.content) == 0

    def __str__(self):
        return str(heapq.nsmallest(len(self.content), [item.element for item in self.content]))

def shortest_path(graph, src, dest):
    """
    Compute the weighted shortest path between two nodes in a directed, weighted graph
    using Dijkstra's algorithm.

    The graph must be a DirectedGraph from the provided graph_library.

    >>> graph = directed_graph_from_dict(
    ...     {'Alice': ['Bob'], 'Bob': ['Carol'], 'Carol': ['Alice']},
    ...     weights={('Alice', 'Bob'): 5, ('Bob', 'Carol'): 5, ('Carol', 'Alice'): 5}
    ... )
    >>> src = graph.get_node_from_name('Carol')
    >>> dest = graph.get_node_from_name('Alice')
    >>> shortest_path(graph, src, dest)
    [Node('Carol'), Node('Alice')]
    """
    INFINITY = float('inf')
    dist = {node: INFINITY for node in graph.nodes} # costs corresponding to the nodes, all other nodes have distances applied to infinity
    dist[src] = 0 # and the source node has distance 0 from source, since its the source.
    visited = set() # keeping visited

    pq = PriorityQueue(sortkey = lambda node: dist[node]) # we want to use distances as the priority.

    pq.add(src)
    parent = {src: None}

    while not pq.is_empty():
        u = pq.poll() # current node that we are expanding.
        if u in visited:
            continue
        visited.add(u)

        for e in graph.get_neighbours(u): # edges that are all leaving the previous node
            v = e.v # the node it is pointing to
            if v in visited:
                continue
            w = e.weight # cost of that node
            new = dist[u] + w # total cost to get to v
            if new < dist[v]:
                dist[v] = new
                parent[v] = u
                pq.add(v)
    return pq


if __name__ == '__main__':
    import doctest
    doctest.testmod()
