#!/usr/bin/python3

import sys
import covariance, standard_deviation

def pearson_correlation(x: list, y: list) -> float:
    """
        Calculates the Pearson Correlation between two arrays.
    """

    if len(x) != len(y):
        print("Dimension Mismatch")
        sys.quit()

    x_std = standard_deviation.standard_deviation(x)
    y_std = standard_deviation.standard_deviation(y)

    pearson = covariance.covariance(x, y)/(x_std * y_std)

    return pearson

