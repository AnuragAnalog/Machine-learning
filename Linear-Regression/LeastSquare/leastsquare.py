#!/usr/bin/python3

"""
    ### Simple Linear Regression ###
    Computes the regression function by taking x and y points, and also
    plots a graph of the line along with the data-points.
"""

import numpy as np
import matplotlib.pyplot as plt

def input_data(n: int) -> (np.array, np.array):
    x = list()
    y = list()

    for i in range(n):
        x.append(float(input("Enter the value of x{}: ".format(i+1))))
        y.append(float(input("Enter the value of y{}: ".format(i+1))))
        print("")
    return np.array(x), np.array(y)

class Regression():
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

    def fitting(self, x: np.array, y: np.array) -> (float, float):
        """
            Computes the regression co-efficients for a simple linear regrssion.
        """
        if len(x) != len(y):
            print("Dimension mismatch of x and y")
            return

        self.__beta = (np.mean(x*y)-np.mean(x)*np.mean(y))/(np.mean(x**2)-np.mean(x)**2)
        self.__alpha = np.mean(y) - (self.__beta * np.mean(x))
        print("The Cost Function with the obtained parameters is", self.__cost_function(x, y))

        return self.__alpha, self.__beta

    def plotting(self, x: np.array, y: np.array, yp: np.array) -> None:
        """
            Gives some of the regrssion plots for analysis
        """
        fig = plt.figure()

        fig.add_subplot(2,1,1)
        plt.plot(x, y, "ro")
        plt.plot(x, yp)

        fig.add_subplot(2,1,2)
        plt.scatter(yp, y-yp)       # Residual plot

        plt.show()

    def analysis(self, x: np.array, y: np.array, yp: np.array, n: int) -> list:
        """
            Does some basic analysis and returns a list of some useful parameters.
        Format of the list is [rse, n-p-1, rsq, adjr2, var_hat]
        """
        if not all(np.array([len(x), len(y), len(yp)]) != n):
            print("Dimension mismatch")
            return

        p = 1 # No. of regressors
        rss = sum((y - yp)**2)
        rse = np.sqrt(rss/(n-p-1))
        tss = sum((y-np.mean(y))**2)
        rsq = 1 - (rss/tss)
        adjr2 = 1 - ((rss/(n-p))/(tss/(n-1)))
        var_hat = rss/(n-2)

        print("Residual sum of squares:",rse,"on",n-p-1,"degrees of freedom.")
        print("R-squared:",rsq)
        print("Adjusted R-squared:",adjr2)

if __name__ == "__main__":	# Only for testing
    n = int(input("Enter the np. of data points: "))
    reg = Regression()
    # x, y = input_data(n)
    x = np.array([23,26,30,34,43,48])
    y = np.array([651,762,856,1063,1190,1298])
    a, b = reg.fitting(x, y)
    yp = lambda x: b*x + a

    print("The regrssion function is: y = x*{} + {}".format(b, a))
