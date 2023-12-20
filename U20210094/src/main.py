#!/usr/bin/env python3

import time
import numpy as np
import matplotlib.pyplot as plt
from Graph import Graph
from Ant import Ant
from SA import SA


def plot_tour(graph, tour, ax, title):
    x, y = zip(*[graph.city_loc[city] for city in tour])
    ax.plot(x, y, c="blue")
    ax.set_title(title)


def plot_all_cities(graph, ax, legend_str):
    x, y = zip(*graph.city_loc)
    ax.scatter(x, y, c="black")
    ax.legend(title=legend_str, loc="upper right")


def main():
    start_time = time.time()
    graph = Graph()

    ACO_par = {"alpha": 18, "beta": 6, "rho": 0.99}
    ant = Ant(graph, **ACO_par)

    aco_runtime = 80
    # print("Starting \tACO")
    ant.ACO(aco_runtime)
    # print(ant.best_cost)

    SA_par = {"init_temp": 10000.0, "num_iter": 100, "cool_rate": 0.995}
    sa = SA(graph, **SA_par)

    sa_runtime = 200
    # print("Starting \t3 Opt Improvement")
    sa._3opt_improvement(ant.best_tour, ant.best_cost, sa_runtime)
    # later can think of doing simulated anealing instead of only tour
    # improvement? maybe not, because will make worse,unneces init temp
    # print(sa.best_cost)

    end_time = time.time()
    # print(f"Time Taken: {end_time - start_time}")

    # # Plotting stuff ------------------------------
    # def legend_str(par: dict):
    #     return ",\n".join([f"{key}: {value}" for key, value in par.items()])

    # aco_legend_str = legend_str(ACO_par)
    # sa_legend_str = "3-opt-improvement"  # legend_str(SA_par)

    # plt.plot(ant.all_costs)
    # plt.legend(title=aco_legend_str)
    # plt.title("ACO's path costs over iterations")
    # plt.show()

    # fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    # plot_tour(
    #     graph,
    #     ant.best_tour,
    #     ax[0],
    #     f"Ant Colony Optimisation (for {aco_runtime}s): {ant.best_cost:.3f}",
    # )

    # plot_tour(
    #     graph,
    #     sa.best_tour,
    #     ax[1],
    #     f"3-opt tour-improvement (for {sa_runtime}s): {sa.best_cost:.3f}",
    # )

    # plot_all_cities(graph, ax[0], aco_legend_str)
    # plot_all_cities(graph, ax[1], sa_legend_str)
    # fig.suptitle("SA on top of ACO")
    # fig.tight_layout()
    # plt.show()


if __name__ == "__main__":
    main()
