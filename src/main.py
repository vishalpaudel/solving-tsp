#!/usr/bin/env python3

from utils import read_test_case

from tsp.Graph import Graph
from tsp.models import Ant, SA



if __name__ == "__main__":
    # The graph reads input when instantiated, (inside Graph::__init__) 

    given_graph = Graph()

    one_ant = Ant(graph)

    i = 0
    n = 10000
    
    one_ant.optimise_once()