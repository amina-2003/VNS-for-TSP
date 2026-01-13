import numpy as np
import random

def swap(solution):
    """Swap two cities."""
    s = solution.copy()
    i, j = random.sample(range(len(s)), 2)
    s[i], s[j] = s[j], s[i]
    return s

def insert(solution):
    """Remove a city and insert it at another position."""
    s = solution.copy()
    i, j = random.sample(range(len(s)), 2)
    city = s.pop(i)
    s.insert(j, city)
    return s

def two_opt(solution):
    """Invert a subsequence of the tour."""
    s = solution.copy()
    i, j = sorted(random.sample(range(len(s)), 2))
    s[i:j] = reversed(s[i:j])
    return s

def get_neighborhoods():
    return [swap, insert, two_opt]
