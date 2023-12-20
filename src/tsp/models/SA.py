"""
Solving TSP with Simulated Annealing
"""


import numpy as np

import time

import numpy as np
import random

from ..Graph import Graph


class SA:
    def __init__(
        self, graph: Graph, *, init_temp: float, num_iter: float, cool_rate: float
    ):
        self.graph = graph

        self.temp = init_temp
        self.num_iter = num_iter
        self.cool_rate = cool_rate

        self.best_cost = np.inf
        self.best_tour = []

        print("Simulated Annealing model instantiated!")

    def simulated_annealing(self, cand_sol: np.ndarray):
        """cand_sol: a starting candidate solution"""
        cur_sol = cand_sol
        cur_cost = self.graph.tour_cost(cand_sol)

        # for the number of iteratations
        cur_iter = 0
        while cur_iter < self.num_iter:
            print(cur_iter, self.num_iter)
            # modify the current tour (in hopes of improvement)
            mod_sol = self.modify_tour(cur_sol)
            mod_cost = self.graph.tour_cost(mod_sol)

            if mod_cost < cur_cost or random.random() < np.exp(
                (cur_cost - mod_cost) / self.temp
            ):
                cur_sol = mod_sol
                cur_cost = mod_cost

            if cur_cost < self.best_cost:
                self.best_tour = cur_sol.copy()
                self.best_cost = cur_cost

            self.temp *= self.cool_rate

            cur_iter += 1

        return self.best_cost, self.best_tour

    def modify_tour(self, cur_tour):
        return self._random_swapping(cur_tour)

    def _3opt_improvement():
        pass

    def _2opt_improvement(self, cur_tour: np.ndarray):
        """
        Performs a random swapping operation of two edges in the current tour.
        """
        pass

    def _random_swapping(self, cur_tour: np.ndarray):
        """
        Perform a random swapping operation of two cities in the current tour.

        Parameters:
            cur_tour (np.ndarray): The current tour represented as a numpy array.

        Returns:
            np.ndarray: The tour after the random swapping operation.
        """
        # Select two distinct random indices
        index1, index2 = random.sample(range(len(cur_tour)), 2)

        # Create a copy of the current tour to avoid modifying it in place
        new_tour = np.copy(cur_tour)

        # Swap the cities at the selected indices
        new_tour[index1], new_tour[index2] = new_tour[index2], new_tour[index1]

        return new_tour


def main():
    # Set parameters
    init_temp = 1000.0
    num_iter = 3
    cool_rate = 0.99995

    graph = Graph()
    one_sim_annel = SA(
        graph, init_temp=init_temp, num_iter=num_iter, cool_rate=cool_rate
    )

    cities = np.arange(graph.num_cities)

    start_time = time.time()

    # Generate an initial solution (random permutation of cities)
    init_sol = list(np.random.permutation(cities))

    one_sim_annel.simulated_annealing(init_sol)

    end_time = time.time()

    # Output the best solution and cost
    print("Best Tour:", one_sim_annel.best_tour)
    print("Best Cost:", one_sim_annel.best_cost)
    print("Time: ", end_time - start_time)


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
