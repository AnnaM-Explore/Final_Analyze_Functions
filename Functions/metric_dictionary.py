import numpy as np
import pandas as pd


def dictionary_of_metrics(items):
    """Input an array of numbers and return a dictionary with calculated metrics as values."""
    arr = np.array(items)

    my_dict = {'mean': round(arr.mean(), 2),
               'median': round(np.median(items), 2),
               'var': round(np.var(items, ddof=1), 2),
               'std': round(np.std(items, ddof=1), 2),
               'min': round(arr.min(), 2),
               'max': round(arr.max(), 2)}
    return my_dict
