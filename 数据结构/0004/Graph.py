class Vertex(object):
    """A Vertex is a node in a graph."""

    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        """Returns a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Edge(tuple):
    """An Edge is a list of two vertices."""

    def __new__(cls, *vs):
        """The Edge constructor takes two vertices."""
        if len(vs) != 2:
            raise ValueError, 'Edges must connect exactly two vertices.'
        return tuple.__new__(cls, vs)

    def __repr__(self):
        """Return a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Graph(dict):
    """A Graph is a dictionary of dictionaries.  The outer
    dictionary maps from a vertex to an inner dictionary.
    The inner dictionary maps from other vertices to edges.
    
    For vertices a and b, graph[a][b] maps
    to the edge that connects a->b, if it exists."""

    def __init__(self, vs=[], es=[]):
        """Creates a new graph.  
        vs: list of vertices;
        es: list of edges.
        """
        for v in vs:
            self.add_vertex(v)
            
        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """Add a vertex to the graph."""
        self[v] = {}

    def add_edge(self, e):
        """Adds and edge to the graph by adding an entry in both directions.

        If there is already an edge connecting these Vertices, the
        new edge replaces it.
        """
        v, w = e
        self[v][w] = e
        self[w][v] = e

    def get_edge(self, v, w):
        """Returns the edge with given two vertices
        if it exists and None otherwise.
        """
        try:
            return self[v][w]
        except KeyError:
            return None

    def remove_edge(self, e):
        """Removes all refierences to the given edge from the graph.
        """
        v, w = e
        self[v].pop(w)
        self[w].pop(v)

    def vertices(self):
        """Returns a list of the vertices in a graph.
        """
        return self.keys()

    def edges(self):
        """Returns a list of edges in a graph.
        """
        ret = set()
        for d in self.itervalues():
            ret.update(d.itervalues())
        return list(ret)

    def out_vertices(self, v):
        """Returns a list of adjacent vertices.
        """
        return self[v].keys()

    def out_edges(self, v):
        """Returns a list of edges connected to the given vertex.
        """
        return self[v].values()

    def add_all_edges(self):
        """Makes a complete graph by adding edges between all pairs of vertices.
        """
        vs = self.vertices()
        for i, v in enumerate(vs):
            for j, w in enumerate(vs):
                if i == j: break
                self.add_edge(Edge(v, w))


def main(script, *args):
    v = Vertex('v')
    #print v
    w = Vertex('w')
    y = Vertex('y')
    #print w
    e = Edge(v, w)
    #print e
    g = Graph([v,w, y], [e])
    #print g
    g.add_all_edges()
    print g


if __name__ == '__main__':
    import sys
    main(*sys.argv)
