import numpy as np

def rel_diff(data_ini, data_end):
    """ calculates percentage relative difference between two vectors"""
    relative_difference = np.abs((data_ini - data_end)/data_ini)*100
    return relative_difference

def rmse(y_obs, y_pred):
    """ calculate the root mean squared error """
    e = np.sqrt(np.sum(((y_obs-y_pred)/y_obs)**2))
    return e