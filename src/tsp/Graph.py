
class Graph:
    def __init__(self, heuristic, num_cities, city_loc, dist_mat):
        self.heuristic = heuristic
        self.num_cities = num_cities
        self.city_loc = city_loc
        self.dist_mat = dist_mat

    def tour_cost(self, tour: np.ndarray) -> float:
        """
        tour: the tour for which the distance is to be calculated
        dist_mat: the distance matrix
        """
        tour_cost = 0.0

        for i in range(self.num_cities):
            tour_cost += self.dist_mat[tour[i], tour[(i + 1) % N]]

        return tour_cost        
