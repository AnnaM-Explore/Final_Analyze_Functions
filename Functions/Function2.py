import numpy as np

"""Define five_num_summary that takes in a list and returns a dictionary. """


def five_num_summary(items):
    """ Use numpy built-ins to find quantiles and assign it quartiles"""
    quartiles = np.quantile(items, [0, 0.25, 0.5, 0.75, 1])
    """ Create dictionary with keys and respective quantiles as values"""
    dicts = {'max': round(quartiles[4], 2),
             'median': round(quartiles[2], 2),
             'min': round(quartiles[0], 2),
             'q1': round(quartiles[1], 2),
             'q3': round(quartiles[3], 2)}
    """ Return a dictionary"""
    return dicts