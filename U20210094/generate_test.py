import random
import math


def generate_euclidean_tsp_test_case(N):
    print("EUCLIDEAN")
    print(N)

    coordinates = []
    for _ in range(N):
        x = round(random.uniform(1, 15), 6)
        y = round(random.uniform(1, 15), 6)
        coordinates.append((x, y))
        print(f"{x} {y}")

    distance_matrix = []
    for i in range(N):
        distances = []
        for j in range(N):
            if i == j:
                distance = 0.0
            else:
                distance = round(
                    math.sqrt(
                        (coordinates[i][0] - coordinates[j][0]) ** 2
                        + (coordinates[i][1] - coordinates[j][1]) ** 2
                    ),
                    6,
                )
            distances.append(distance)
        distance_matrix.append(distances)
        print(" ".join(map(str, distances)))


generate_euclidean_tsp_test_case(300)
