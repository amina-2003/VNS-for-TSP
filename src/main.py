import numpy as np
from instance import load_instance
from vns import vns
import pandas as pd

if __name__ == "__main__":
    distance_matrix = load_instance("data/tsp_10cities.csv")
    n_cities = distance_matrix.shape[0]
    initial_solution = list(np.random.permutation(n_cities))
    
    best_solution = vns(initial_solution, distance_matrix, max_iter=500)
    print("Best solution found:", best_solution)
    from utils import tour_cost
    print("Cost:", round(tour_cost(best_solution, distance_matrix),2))
