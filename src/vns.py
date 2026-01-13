from neighborhoods import get_neighborhoods
from local_search import local_search
from utils import tour_cost

import random

def shake(solution, neighborhood):
    return neighborhood(solution)

def vns(initial_solution, distance_matrix, max_iter=100):
    neighborhoods = get_neighborhoods()
    best = initial_solution
    for t in range(max_iter):
        k = 0
        while k < len(neighborhoods):
            s_shaken = shake(best, neighborhoods[k])
            s_local = local_search(s_shaken,distance_matrix, neighborhoods, max_iter=100)
            if tour_cost(s_local, distance_matrix) < tour_cost(best, distance_matrix):
                best = s_local
                k = 0
            else:
                k += 1
    return best
