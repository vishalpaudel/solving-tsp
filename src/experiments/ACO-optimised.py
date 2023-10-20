#!/usr/bin/env python3

import random
import numpy as np
import time

import sys

# Read inputs
lines = sys.stdin.read().strip().split("\n")
heuristic = lines[0].strip()
N = int(lines[1])
data_lines = lines[2:]

# Split and parse the data into C and D
data = [list(map(float, line.split())) for line in data_lines]
C = np.array(data[:N])
D = np.array(data[N:])
cities = np.arange(N)

# Constants
alpha = 2.5
beta = 2.5
rho = 0.25

# Precompute P using NumPy
P = np.where(D == 0, 0, 1 / (D**alpha))
np.fill_diagonal(P, 0.0)


# Helper functions
def calculate_tour_cost(tour):
    return np.sum(D[tour, np.roll(tour, -1)])


# Initialize R with 1s
R = np.ones((N, N))


def probability(u, v):
    s = np.sum(P[u, cities != u] * R[u, cities != u] ** beta)
    P[u, v] = (P[u, v] * R[u, v] ** beta) / (s + np.finfo(float).eps)


def reward(u, v, tour_cost):
    R[u, v] = (1 - rho) * R[u, v] + 1 / tour_cost


# Ant tour function
def make_the_ant_traverse():
    start_city = random.choice(cities)
    current_city = start_city
    remaining_cities = np.delete(cities, current_city)
    tour = [start_city]

    while remaining_cities.size:
        probabilities_of_transition = P[current_city, remaining_cities]
        if np.sum(probabilities_of_transition) == 0:
            next_city = random.choice(remaining_cities)
        else:
            next_city = np.random.choice(
                remaining_cities,
                p=probabilities_of_transition / np.sum(probabilities_of_transition),
            )
        remaining_cities = np.delete(
            remaining_cities, np.where(remaining_cities == next_city)
        )
        tour.append(next_city)
        probability(current_city, next_city)
        current_city = next_city

    return tour


# Main optimization loop
num_iterations = 100000
list_of_tours = []
best_tour = 0
best_cost = float("inf")

start_time = time.time()
end_time = start_time
total_time = 10

while (end_time - start_time) < (total_time):
    latest_tour = make_the_ant_traverse()
    list_of_tours.append(latest_tour)
    cost_of_tour = calculate_tour_cost(latest_tour)
    if cost_of_tour < best_cost:
        best_cost = cost_of_tour
        best_tour = latest_tour

    u = latest_tour[-1]
    v = latest_tour[0]
    reward(u, v, cost_of_tour)

    end_time = time.time()

print("***************")
print(best_tour, best_cost)
print(end_time - start_time)
