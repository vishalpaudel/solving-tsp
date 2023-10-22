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

        self.init_temp = init_temp
        self.num_iter = num_iter
        self.cool_rate = cool_rate

    def simulated_annealing(self, cand_sol: np.ndarray):
        """cand_sol: a starting candidate solution"""
        # modify the current tour (in hopes of improvement)
        modified_tour = self.modify_tour()

    def modify_tour(self, cur_tour):
        return

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
    cities = np.arange(N)

    # Set parameters
    initial_temperature = 1000.0
    num_iterations = 300000
    cooling_rate = 0.99995

    start_time = time.time()

    # Generate an initial solution (random permutation of cities)
    init_sol = list(np.random.permutation(cities))

    # Apply simulated annealing
    best_solution, best_cost = simulated_annealing(init_sol)

    end_time = time.time()

    # Output the best solution and cost
    print("Best Tour:", best_solution)
    print("Best Cost:", best_cost)
    print("Time: ", end_time - start_time)


if __name__ == "__main__":
    main()
