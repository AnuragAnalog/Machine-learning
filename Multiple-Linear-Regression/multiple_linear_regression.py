#!/usr/bin/python3

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

class Multiple_Linear_Regression():
    """
        Fit a linear model which tries to reduce the residual sum of squares
    between the observed values and the predicted values.
    """

    def __init__(self):
        self.coef = list()

    def __str__(self):
        return "Multiple_Linear_Regression(Co-effients are: "+str(self.coef)+")"

    def get_params(self):
        """
        Returns
        -------
        coef : ndarray
            returns an 1-d array of coefficients
        """

        return self.coef

    def fit(self, X, y):
        """
        Parameters
        ----------
        X : ndarray, list
            A n-d array which represents the features.
        y : ndarray, list
            An 1-d array which represents the labels

        Returns
        -------
        None : NoneType
        """

        X = np.array(X)
        self.coef = np.dot(np.dot(np.linalg.pinv(np.dot(X.transpose(), X)), X.transpose()), y)

        return

    def predict(self, x_new):
        """
        Parameters
        ----------
        x_new : ndarray, list
            An 1-d array which represents the features of an observation

        Returns
        -------
        y_hat : float
            Predicted value of the given observation
        """

        x_new = np.array(x_new)
        y_hat = np.dot(self.coef, x_new)

        return y_hat

if __name__ == "__main__":
    pass