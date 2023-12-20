#!/usr/bin/env python3

import numpy as np
import sys

import math
import random


def read_test_case():
    # Reading input
    # heuristic = input().strip()
    # num_cities = int(input().strip())
    # city_loc = [list(map(float, input().strip().split())) for _ in range(N)]
    # dist_mat = [list(map(float, input().strip().split())) for _ in range(N)]

    # Read input and split into lines
    lines = sys.stdin.read().strip().split("\n")

    # Extract relevant information
    heuristic = lines[0].strip()
    num_cities = int(lines[1])
    data_lines = lines[2:]

    # Split and parse the data into city_loc(ations) and dist_mat(rix)
    data = [list(map(float, line.split())) for line in data_lines]
    city_loc, dist_mat = np.array(data[:num_cities]), np.array(data[num_cities:])

    return heuristic, num_cities, city_loc, dist_mat


def gen_euclidean_test_case(N):
    # Print the problem type and the number of cities
    print("EUCLIDEAN")
    print(N)

    # Generate random coordinates for N cities
    coordinates = [
        (round(random.uniform(1, 15), 6), round(random.uniform(1, 15), 6))
        for _ in range(N)
    ]

    # Print the generated coordinates
    for x, y in coordinates:
        print(f"{x} {y}")

    # Initialize the distance matrix with zeros
    distance_matrix = [[0.0] * N for _ in range(N)]

    # Calculate distances between city pairs and populate the distance matrix
    for i in range(N):
        for j in range(i + 1, N):
            distance = round(
                math.sqrt(
                    (coordinates[i][0] - coordinates[j][0]) ** 2
                    + (coordinates[i][1] - coordinates[j][1]) ** 2
                ),
                6,
            )
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance

    # Print the distance matrix
    for row in distance_matrix:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    num_cities = 20
    gen_euclidean_test_case(num_cities)
