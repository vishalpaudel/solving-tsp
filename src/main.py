#!/usr/bin/env python3

from tsp.Graph import Graph
from tsp.models.Ant import Ant

if __name__ == "__main__":
    # The graph reads input when instantiated, (inside Graph::__init__)

    given_graph = Graph()

    one_ant = Ant(given_graph)

    i = 0
    n = 10000

    one_ant.optimise_once()
