"""
Solving TSP with Simulated Annealing
"""

from time import time
import numpy as np
from numpy import inf, exp, random, arange

from Graph import Graph


class SA:
    def __init__(
        self, graph: Graph, init_temp: float, num_iter: float, cool_rate: float
    ):
        _start_time = time()
        self.graph = graph
        self.temp = init_temp
        self.num_iter = num_iter
        self.cool_rate = cool_rate
        self.best_cost = inf
        self.best_tour = []
        _end_time = time()
        _elapsed_time = _end_time - _start_time
        # print(f"\nTook {_elapsed_time:.5f} to create \tSimAnneal")

    def simulated_annealing(self, cand_sol, best_cost, runtime):
        cur_sol = np.array(cand_sol)
        cur_cost = self.graph.tour_cost(cand_sol)
        self.best_cost = best_cost
        start = time()
        end = start
        while (end - start) < runtime:
            mod_sol = self.modify_tour(cur_sol)
            mod_cost = self.graph.tour_cost(mod_sol)
            if mod_cost < cur_cost or random.random() < exp(
                (cur_cost - mod_cost) / self.temp
            ):
                cur_sol = mod_sol
                cur_cost = mod_cost
            if cur_cost < self.best_cost:
                self.best_tour = cur_sol.copy()
                self.best_cost = cur_cost
                print(self.best_cost)
            self.temp *= self.cool_rate
            end = time()
        return self.best_cost, self.best_tour

    def modify_tour(self, cur_tour):
        return self._random_swapping(cur_tour)

    def _3opt_improvement(self, cur_tour, cost, runtime):
        start_tour = cur_tour
        n = len(cur_tour)
        _start_time = time()
        _end_time = time()
        _elapsed_time = _end_time - _start_time
        while _elapsed_time < runtime:
            # cur_tour = start_tour
            for i in range(1, n - 1):
                for j in range(i + 1, n):
                    for k in range(j + 1, n + 1):
                        new_tour = self._three_opt_swap(cur_tour, i, j, k)
                        new_distance = self.graph.tour_cost(new_tour)
                        if new_distance < self.best_cost:
                            cur_tour = new_tour
                            self.best_tour = new_tour
                            self.best_cost = new_distance
                            # print(self.best_cost)
                            print(" ".join(map(str, self.best_tour)))
                        if time() - _start_time > runtime:
                            return
            _end_time = time()
            _elapsed_time = _end_time - _start_time

    def _three_opt_swap(self, tour, i, j, k):
        new_tour = np.copy(tour)
        new_tour[i:j] = np.flip(tour[i:j])
        new_tour[j:k] = np.flip(tour[j:k])
        return new_tour

    def _random_swapping(self, cur_tour):
        indices = random.choice(len(cur_tour), 2, replace=False)
        new_tour = np.copy(cur_tour)
        new_tour[indices[0]], new_tour[indices[1]] = (
            new_tour[indices[1]],
            new_tour[indices[0]],
        )
        return new_tour


def main():
    init_temp = 1000.0
    num_iter = 3
    cool_rate = 0.99995

    graph = Graph()
    one_sim_annel = SA(
        graph, init_temp=init_temp, num_iter=num_iter, cool_rate=cool_rate
    )

    cities = arange(graph.num_cities)
    _start_time = time()
    init_sol = random.permutation(cities)
    one_sim_annel.simulated_annealing(init_sol, inf, 60)
    _end_time = time()
    _elapsed_time = _end_time - _start_time
    print("Best Tour:", one_sim_annel.best_tour)
    print("Best Cost:", one_sim_annel.best_cost)
    print("Time: ", _elapsed_time)


if __name__ == "__main__":
    main()
