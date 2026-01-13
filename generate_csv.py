import pandas as pd
import numpy as np

# Nombre de villes
n = 10

# Coordonnées aléatoires (pour visualisation)
coords = np.random.rand(n, 2) * 100

# Calcul de la matrice des distances Euclidiennes
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        dist_matrix[i, j] = np.linalg.norm(coords[i] - coords[j])

# Créer un DataFrame et sauvegarder
df = pd.DataFrame(dist_matrix, index=[f"City{i}" for i in range(n)],
                  columns=[f"City{i}" for i in range(n)])
df.to_csv("data/tsp_10cities.csv")

# Sauver les coordonnées pour affichage
coords_df = pd.DataFrame(coords, columns=["x", "y"], index=[f"City{i}" for i in range(n)])
coords_df.to_csv("data/tsp_10cities_coords.csv")

print("TSP instance and coordinates saved in 'data/' folder")
