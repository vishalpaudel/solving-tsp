import numpy as np
from .Graph import Graph

class Ant:
    def __init__(self, graph: Graph, *, alpha: float = 2.5, beta: float=2.5, rho: float=0.25):
        self.graph = graph
        self.num_cities = graph.num_cities

        # parameters
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
