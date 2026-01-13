from neighborhoods import get_neighborhoods
from utils import tour_cost

def local_search(solution,distance_matrix, neighborhoods=None, max_iter=100):
    """Simple local search: apply neighborhoods repeatedly."""
    if neighborhoods is None:
        neighborhoods = get_neighborhoods()
    best = solution
    for _ in range(max_iter):
        improved = False
        for n in neighborhoods:
            candidate = n(best)
            if tour_cost(candidate,distance_matrix) < tour_cost(best,distance_matrix):
                best = candidate
                improved = True
        if not improved:
            break
    return best
