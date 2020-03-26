#!/usr/bin/python3

import numpy as np
from matplotlib import pyplot as plt

from leastsquare import Regression

def plotting(x: np.array, y: np.array, a: float, b: float) -> None:
    yp = a + b * x

    fig = plt.figure()
    fig.add_subplot(2,1,1)
    plt.plot(x, y, "ro")
    plt.plot(x, yp)

    fig.add_subplot(2,1,2)
    plt.scatter(yp, y-yp)       # Residual plot

    plt.show()

    return

if __name__ == '__main__':
    reg = Regression()
    x = np.array([23,26,30,34,43,48])
    y = np.array([651,762,856,1063,1190,1298])
    a, b = reg.fitting(x, y)

    plotting(x, y, a, b)

    print("The regression function is: y = x*{} + {}".format(b, a))