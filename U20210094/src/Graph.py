import numpy as np

from utils import read_test_case
from time import time


class Graph:
    def __init__(self):
        _start_time = time()

        heuristic, num_cities, city_loc, dist_mat = read_test_case()
        self.heuristic = heuristic
        self.num_cities = num_cities
        self.city_loc = city_loc
        self.dist_mat = dist_mat

        _end_time = time()
        # print(f"\nTook {_end_time - _start_time:.5f} to create \tGraph!")

    def tour_cost(self, tour: np.ndarray) -> float:
        """
        tour: the tour for which the distance is to be calculated
        dist_mat: the distance matrix
        """
        _cost = 0.0
        for i in range(self.num_cities):
            _cur_city = tour[i]
            _next_city = tour[(i + 1) % self.num_cities]

            _cost += self.dist_mat[_cur_city, _next_city]

        return _cost
