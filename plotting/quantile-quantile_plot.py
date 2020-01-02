#!/usr/bin/python3

"""
    Quantile-Quantile (Q-Q) Plot
    Which is used to see whether two given data-sets come from same distribution or not.
    There is no restriction that the two distributions should contain equal number of data-points.
"""

import sys
import numpy as np
import matplotlib.pyplot as plt

def qqplot(data1: np.array, data2: np.array) -> None:
    if np.prod(data1.shape) != len(data1):
        print("Data1 should be only one-dimensional.")
        sys.exit()

    if np.prod(data2.shape) != len(data2):
        print("Data2 should be only one-dimensional.")
        sys.exit()

    n = 100
    if len(data1) > n and len(data2) > n:
        qbin = [i/n for i in range(1, n+1)]
        x = np.quantile(data1, qbin)
        y = np.quantile(data2, qbin)
    elif len(data1) <= n or len(data2) <= n:
        bin = min(len(data1), len(data2))
        qbin = [i/bin for i in range(1, bin+1)]
        if len(data1) <= n:
            x = data1
            y = np.quantile(data2, qbin)
        else:
            x = np.quantile(data1, qbin)
            y = data2

    line1 = list(np.quantile(x, [0.25,0.75]))
    line2 = list(np.quantile(y, [0.25,0.75]))

    m = np.diff(line2)/np.diff(line1)
    c = line2[0] - m*line1[0]

    line1.insert(0, x[0])
    line1.insert(-1, x[-1])
    line2.insert(0, m*x[0]+c)
    line2.insert(-1, m*x[-1]+c)

    plt.plot(x, y, 'ro')
    plt.plot(line1, line2, linewidth=2.5)
    plt.show()

if __name__ == '__main__':
    d1 = np.random.beta(1, 2, size=1000)
    d2 = np.random.randn(1000,1)

    qqplot(d1, d2)
