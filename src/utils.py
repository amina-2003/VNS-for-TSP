import numpy as np
import matplotlib.pyplot as plt

def tour_cost(solution, distance_matrix=None):
    if distance_matrix is None:
        raise ValueError("distance_matrix is required")
    cost = 0
    for i in range(len(solution)):
        cost += distance_matrix[solution[i-1], solution[i]]
    return cost

def plot_tour(solution, coords, title="Tour"):
    x = [coords[i][0] for i in solution] + [coords[solution[0]][0]]
    y = [coords[i][1] for i in solution] + [coords[solution[0]][1]]
    plt.figure(figsize=(6,6))
    plt.plot(x, y, marker='o')
    plt.title(title)
    plt.show()
