import pandas as pd
import numpy as np

def load_instance(file_path):
    """Load TSP instance from CSV file and return distance matrix."""
    df = pd.read_csv(file_path, index_col=0, sep=",")
    return df.values
