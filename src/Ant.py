import numpy as np
from Graph import Graph

class Ant:
    def __init__(
        self, graph: Graph, *, alpha: float=2.5, beta: float=2.5, rho: float=0.25
    ):
        self.graph = graph
        self.num_cities = graph.num_cities
        self.dist_mat = graph.dist_mat

        # Probability and Reward Values
        self.P = np.where(self.dist_mat == 0, 0, 1 / (self.dist_mat ** alpha))
        np.fill_diagonal(self.P, 0.0)
        self.R = np.ones((self.num_cities, self.num_cities))

        # Parameters for ACO
        self.alpha = alpha
        self.beta = beta
        self.rho = rho

        self.cities = np.arange(self.num_cities)

    def ACO(self):
        print(self.traversal())

    # Helper functions
    def calculate_tour_cost(self, tour):
        return np.sum(self.dist_mat[tour, np.roll(tour, -1)])

    def probability(self, u, v):
        s = np.sum(self.P[u, self.cities != u] * self.R[u, self.cities != u] ** self.beta)
        self.P[u, v] = ((1 / (self.dist_mat[u, v] ** self.alpha)) * (self.R[u, v] ** self.beta)) / (s + np.finfo(float).eps)

    def reward(self, u, v, tour_cost):
        self.R[u, v] = (1 - self.rho) * self.R[u, v] + (1 / tour_cost)

    def traversal(self):
        cities_copy = self.cities.copy()
        start = np.random.choice(cities_copy)
        current_city = start
        np.delete(cities_copy, start)

        tour = [start]
        while cities_copy.size:
            probabilities_of_transition = self.P[current_city, cities_copy]
            if np.sum(probabilities_of_transition) == 0:
                next_city = np.random.choice(cities_copy)
            else:
                next_city = np.random.choice(
                    cities_copy,
                    p=probabilities_of_transition / np.sum(probabilities_of_transition),
                )
            remaining_cities = np.delete(
                cities_copy, np.where(cities_copy == next_city)
            )
            tour.append(next_city)
            self.probability(current_city, next_city)
            current_city = next_city
        return tour
            
    def optimise_once(self):
        pass


if __name__ == "__main__":

    graph = Graph()
    ant = Ant(graph)
 
    ant.ACO()