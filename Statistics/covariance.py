#!/usr/bin/python3

import sys
import mean

def covariance(x: list, y: list) -> float:
    """
        Calculates the co-variance between two arrays.
    """

    if len(x) != len(y):
        print("Dimension Mismatch")
        sys.quit()

    x_mean = mean.mean(x)
    y_mean = mean.mean(y)
    cov = 0

    for xi, yi in zip(x, y):
        cov = cov + ((xi - x_mean) * (yi - y_mean))

    return cov/(len(x)-1)


