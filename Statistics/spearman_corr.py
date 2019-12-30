#!/usr/bin/python3

import numpy as np

def spearman_corr(x: list, y: list) -> float:
    """
        Calculates the Spearman-rank correlation between the given two list.
    """

    if len(x) != len(y):
        print("Dimension Mismatch")
        print("Length of x and y should be same")
        sys.exit()

    tmp = sorted(zip(x, y, range(1, len(y)+1)))

    rgx = range(1, len(x)+1)
    rgy = list()
    for i in range(len(y)):
        rgy.append(tmp[i][2])

    tmp = np.cov(rgx, rgy)
    corr = tmp[0][1]/tmp[0][0]

    return corr
