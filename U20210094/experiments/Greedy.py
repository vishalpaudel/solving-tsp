import numpy as np
from Graph import Graph


def Greedy(graph: Graph):
    N, D = graph.num_cities, graph.dist_mat
    visited = np.full(N, False, dtype=bool)
    current_city = 0
    tour = [current_city]
    visited[current_city] = True
    total_distance = 0

    for _ in range(N - 1):
        nearest_city = None
        min_distance = float("inf")
        for city in range(N):
            if not visited[city] and D[current_city][city] < min_distance:
                nearest_city = city
                min_distance = D[current_city][city]
        tour.append(nearest_city)
        visited[nearest_city] = True
        total_distance += min_distance
        current_city = nearest_city

    # Return to the starting city to complete the tour
    total_distance += D[current_city][tour[0]]
    print(total_distance)
    return tour, total_distance
