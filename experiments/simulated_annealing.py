"""
Solving TSP with Simulated Annealing
"""

import sys
import numpy as np
import random
import math

import time


def calculate_tour_cost(tour, distances):
    cost = 0.0
    N = len(tour)
    for i in range(N):
        cost += distances[tour[i], tour[(i + 1) % N]]
    return cost


def simulated_annealing(
    distances, initial_solution, temperature, cooling_rate, num_iterations
):
    current_solution = initial_solution.copy()
    current_cost = calculate_tour_cost(current_solution, distances)
    best_solution = current_solution.copy()
    best_cost = current_cost

    for _ in range(num_iterations):
        i, j = random.sample(range(len(current_solution)), 2)
        neighbor_solution = current_solution.copy()
        neighbor_solution[i], neighbor_solution[j] = (
            neighbor_solution[j],
            neighbor_solution[i],
        )
        neighbor_cost = calculate_tour_cost(neighbor_solution, distances)

        if neighbor_cost < current_cost or random.random() < math.exp(
            (current_cost - neighbor_cost) / temperature
        ):
            current_solution = neighbor_solution
            current_cost = neighbor_cost

        if current_cost < best_cost:
            best_solution = current_solution.copy()
            best_cost = current_cost

        temperature *= cooling_rate

    return best_solution, best_cost


def main():
    lines = sys.stdin.read().strip().split("\n")

    # Read the distance measure type (heuristic) and the number of cities (N)
    heuristic = lines[0].strip()
    N = int(lines[1])

    # Parse the coordinates and distances
    data = [list(map(float, line.split())) for line in lines[2:]]

    # Split the data into C and D
    C = np.array(data[:N])
    D = np.array(data[N:])

    cities = np.arange(N)

    # Set parameters
    initial_temperature = 1000.0
    num_iterations = 300000
    cooling_rate = 0.99995

    start_time = time.time()

    # Generate an initial solution (random permutation of cities)
    initial_solution = list(np.random.permutation(cities))

    # Apply simulated annealing
    best_solution, best_cost = simulated_annealing(
        D, initial_solution, initial_temperature, cooling_rate, num_iterations
    )

    end_time = time.time()

    # Output the best solution and cost
    print("Best Tour:", best_solution)
    print("Best Cost:", best_cost)
    print("Time: ", end_time - start_time)


if __name__ == "__main__":
    main()
