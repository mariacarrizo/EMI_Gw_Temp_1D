import numpy as np

def rel_diff(data_ini, data_end):
    """ calculates percentage relative difference between two vectors"""
    relative_difference = np.abs((data_ini - data_end)/data_ini)*100
    return relative_difference