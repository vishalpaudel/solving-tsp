import numpy as np
from ..Graph import Graph

class Ant:
    def __init__(self, graph: Graph, *, alpha: float = 2.5, beta: float=2.5, rho: float=0.25):
        self.graph = graph
        self.num_cities = graph.num_cities
        self.dist_mat = graph.dist_mat

        # Probability and Reward Values
        self.P = np.where(self.dist_mat == 0, 0, 1 / (self.dist_mat ** alpha))
        np.fill_diagonal(P, 0.0)
        self.R = np.ones((self.num_cities, self.num_cities))

        # Parameters for ACO
        self.alpha = alpha
        self.beta = beta
        self.rho = rho

        s

    def ACO(self):
        pass

    # Helper functions
    def calculate_tour_cost(self, tour):
        return np.sum(self.dist_mat[tour, np.roll(tour, -1)])

    def probability(self, u, v):
        s = np.sum(self.P[u, cities != u] * self.R[u, cities != u] ** self.beta)
        self.P[u, v] = (self.P[u, v] * self.R[u, v] ** self.beta) / (s + np.finfo(float).eps)

    def optimise_once(self):
        pass
