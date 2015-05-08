from Graph import *
import random


class RandomGraph(Graph):
    """An Erdos-Renyi random graph is a Graph where the probability
    of an edge between any two nodes is p.
    """
    def add_random_edges(self, p):
        """Add edges at random so that the probability is p that
        there is an edge between any two nodes.
        """
        for i, v in enumerate(self.vs):
            for j, w in enumerate(self.vs):
                if j <= i: continue
                if random.random() > p: continue
                self.add_edge(Edge(w, v))

