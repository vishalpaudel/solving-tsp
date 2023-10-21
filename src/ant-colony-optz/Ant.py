import numpy as np


class Ant:
    def __init__(self, graph, alpha=2.5, beta=2.5, rho=0.25):
        self.graph = graph
        self.num_cities = len(graph)

        self.N = graph.num_cities
        self.D = graph.distance_matrix

        self.P = np.where(self.D == 0, 0, 1 / (self.D**alpha))
        np.fill_diagonal(self.P, 0.0)

        self.R = np.ones((self.N, self.N))

        # parameters
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
