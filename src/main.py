#!/usr/bin/env python3

from utils import read_test_case

from tsp.Graph import Graph

if __name__ == "__main__":
    heuristic, num_cities, city_loc, dist_mat = read_test_case()

    given_graph = Graph(heuristic, num_cities, city_loc, dist_mat)
