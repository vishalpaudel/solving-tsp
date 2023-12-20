from numpy import random, ones, where, fill_diagonal, arange, finfo, delete, zeros
from time import time
import warnings

warnings.filterwarnings("ignore")


class Ant:
    def __init__(self, graph, alpha, beta, rho):
        _start_time = time()

        self.graph = graph
        self.num_cities = graph.num_cities
        self.dist_mat = graph.dist_mat

        self.best_tour, self.best_cost = 0, float("inf")

        self.P = where(
            self.dist_mat == 0, 0, 1 / (self.dist_mat**alpha + finfo(float).eps)
        )
        fill_diagonal(self.P, 0.0)
        self.R = ones((self.num_cities, self.num_cities))

        self.alpha = alpha
        self.beta = beta
        self.rho = rho

        self.cities = arange(self.num_cities)

        self.all_tours = []
        self.best_tours = []

        self.all_costs = []

        _end_time = time()
        # print(f"\nTook {_end_time - _start_time:.5f} to create \tAnt!")

    def ACO(self, runtime):
        _start_time = time()
        _end_time = _start_time

        _elapsed_time = _end_time - _start_time
        while _elapsed_time < runtime:
            tour = self.traversal()
            tour_cost = self.graph.tour_cost(tour)
            self.all_costs.append(tour_cost)
            if tour_cost < self.best_cost:
                self.best_tour = tour
                self.best_cost = tour_cost
                # print(self.best_cost)
                print(" ".join(map(str, self.best_tour)))
            self.all_tours.append(tour)
            self.best_tours.append(self.best_tour)
            u = tour[-1]
            v = tour[0]
            self.reward(u, v, tour_cost)

            _end_time = time()
            _elapsed_time = _end_time - _start_time

    def probability(self, u, v):
        s = sum(self.P[u, self.cities != u] * self.R[u, self.cities != u] ** self.beta)
        self.P[u, v] = (
            (1 / (self.dist_mat[u, v] ** self.alpha)) * (self.R[u, v] ** self.beta)
        ) / (s + finfo(float).eps)

    def reward(self, u, v, tour_cost):
        self.R[u, v] += (1 - self.rho) * self.R[u, v] + (1 / tour_cost)

    def traversal(self):
        cities_copy = self.cities
        start_city = random.choice(cities_copy)
        current_city = start_city
        cities_copy = delete(cities_copy, where(cities_copy == start_city))

        tour = zeros(self.num_cities, dtype=int)
        tour[0] = start_city
        i = 0
        while cities_copy.size:
            probs_of_transition = self.P[current_city, cities_copy]
            if sum(probs_of_transition) == 0:
                next_city = random.choice(cities_copy)
            else:
                next_city = random.choice(
                    cities_copy,
                    p=probs_of_transition / sum(probs_of_transition),
                )
            cities_copy = delete(cities_copy, where(cities_copy == next_city))

            i += 1
            tour[i] = next_city
            self.probability(current_city, next_city)
            current_city = next_city

        return tour
