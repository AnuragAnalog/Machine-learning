#!/usr/bin/python3

import numpy as np

class Regression():
    """
        ### Simple Linear Regression ###
        Computes the regression function by taking x and y points, and also
        plots a graph of the line along with the data-points.
    """

    def __init__(self) -> None:
        self.__alpha = 0.0
        self.__beta = 0.0

    def __str__(self) -> str:
        if self.__beta >= 0:
            return 'Regression Line\n'+str(self.__alpha)+' + '+str(self.__beta)+' x'
        else:
            return 'Regression Line\n'+str(self.__alpha)+str(self.__beta)+' x'

    def __cost_function(self, x: np.array, y: np.array) -> float:
        """
            Calculates the cost of the given regression line.
        """
        if len(x) != len(y):
            print("Dimension mismatch of x and y")
            return

        J = 0
        for (xi, yi) in zip(x, y):
            J = J + (yi - (self.__beta*xi - self.__alpha))**2
        J = J/len(x)

        return J

    def __analysis(self, x: np.array, y: np.array) -> list:
        # Does some basic analysis and returns a list of some useful parameters. Format of the list is [self.rse, n-p-1, rsq, adjr2, var_hat]

        yp = self.__alpha + self.__beta * x

        p = 1 # No. of regressors
        self.rss = sum((y - yp)**2)
        self.rse = np.sqrt(self.rss/(self.data_length - p - 1))
        self.tss = sum((y - np.mean(y))**2)
        self.rsq = 1 - (self.rss/self.tss)
        self.adjr2 = 1 - ((self.rss/(self.data_length - p))/(self.tss/(self.data_length - 1)))
        self.var_hat = self.rss/(self.data_length - 2)

        return

    def get_rss(self):
        """
        Returns
        -------
        rss : float
            Calculated Residual square sum
        """

        return self.rss

    def get_tss(self):
        """
        Returns
        -------
        tss : float
            Calculated Total square sum
        """

        return self.tss

    def get_rse(self):
        """
        Returns
        -------
        rse : float
            Calculated Residual square Error
        """

        return self.rse

    def get_rsquare(self):
        """
        Returns
        -------
        rsq : float
            Calculated R^2
        """

        return self.rsq

    def get_adjustedr2(self):
        """
        Returns
        -------
        adjr2 : float
            Calculated Adjusted R^2
        """

        return self.adjr2

    def get_estimated_variance(self):
        """
        Returns
        -------
        var_hat : float
            Calculated estimate variance
        """

        return self.var_hat

    def fitting(self, x: np.array, y: np.array) -> (float, float):
        """
        Computes the regression co-efficients for a simple linear regself.rssion.

        Parameters
        ----------
        x : ndarray
            An array which represents features of the data
        y : ndarray, list
            An array which represents labels of the data

        Returns
        -------
        __alpha : float
            Intercept of the linear model
        __beta : float
            Slope of the linear model
        """

        if len(x) != len(y):
            print("Dimension mismatch of x and y")
            return

        self.data_length = len(x)

        self.__beta = (np.mean(x*y)-np.mean(x)*np.mean(y))/(np.mean(x**2)-np.mean(x)**2)
        self.__alpha = np.mean(y) - (self.__beta * np.mean(x))
        print("The Cost Function with the obtained parameters is", self.__cost_function(x, y))

        return self.__alpha, self.__beta

    def predict(self, x_new):
        """
        Predicting the value of a new observation

        Parameters
        ----------
        x_new : float
            A new observation

        Returns
        -------
        y_hat : float
            Predicted value
        """

        y_hat = self.__alpha + self.__beta * x_new

        return y_hat

if __name__ == "__main__":	# Only for testing
    reg = Regression()
    x = np.array([23,26,30,34,43,48])
    y = np.array([651,762,856,1063,1190,1298])
    a, b = reg.fitting(x, y)

    print("The regression function is: y = x*{} + {}".format(b, a))
