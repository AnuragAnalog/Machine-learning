#!/usr/bin/python3

import mean
import numpy as np

def standard_deviation(array: list) -> float:
    """
        Calculates the Variance of a given array, which gives the speread of the distribution.
    """

    arr_mean = mean.mean(array)
    var = 0

    for element in array:
        var = var + (element - arr_mean)**2

    return np.sqrt(var/len(array))
