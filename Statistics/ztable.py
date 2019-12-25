#!/usr/bin/python3

import numpy as np
import pandas as pd
import scipy.integrate

from pandas import DataFrame

"""
    Z-table values are calculated using the cumulative distribution function of a standard normal distribution with mean of zero and standard deviation of one.
"""

def ztable() -> pd.DataFrame:
    """
        Ф(z) = (1/sqrt(2*pi))∫e^{-(t^2)/2}dt from -infinity to z
    """

    ztable = [[0 for i in range(10)] for j in range(41)]

    phi = lambda x: (np.exp(-1*(x**2)/2))/(np.sqrt(2*np.pi))
    for i in range(41):
        for j in range(10):
            z = i/10+j/100
            ztable[i][j] = scipy.integrate.quad(phi, -1*np.inf, z)[0]

    return pd.DataFrame(ztable, index=np.arange(0,4.1,0.1), columns=np.arange(0,0.1,0.01))

