#!/usr/bin/python3

"""
    ### Simple Linear Regression ###
    Computes the regression coefficients using the gradient descent method
"""

import numpy as np
import matplotlib.pyplot as plt

def input_data(self, n: int) -> (np.array, np.array):
    x = list()
    y = list()

    for i in range(n):
        x.append(float(input("Enter the value of x{}: ".format(i+1))))
        y.append(float(input("Enter the value of y{}: ".format(i+1))))
        print("")
    return np.array(x), np.array(y)

class Gradent_descent():
    """
    Fit a linear model using gradient descent
    """
    def __init__(self) -> None:
        self.__alpha = 0.0
        self.__beta = 0.0
        self.__learning_rate = 0.01

    def __str__(self) -> str:
        if self.__beta >= 0:
            return 'Regression Line\n'+str(self.__alpha)+' + '+str(self.__beta)+' x'
        else:
            return 'Regression Line\n'+str(self.__alpha)+str(self.__beta)+' x'

    def __cost_function(self, x: np.array, y: np.array) -> float:
        # Calculates the cost of the given regression line.
        if len(x) != len(y):
            print("Dimension mismatch of x and y")
            return

        J = 0
        for (xi, yi) in zip(x, y):
            J = J + (yi - (self.__beta*xi - self.__alpha))**2
        J = J/len(x)

        return J

    def fitting(self, x: np.array, y: np.array, alpha: float =None, beta: float =None, learning_rate: float =None, iterate: int =True) -> (float, float):
        """
        Fit a linear model

        Parameters
        ----------
        x : ndarray, list
            A 1-d array which represents features array of the data
        y : ndarray, list
            A 1-d array which represents labels of the data
        alpha : float, default None
            Intercept of the model
        beta : float, default None
            Slope of the model
        learning_rate : float, default None
            Learning rate for the convergence
        iterate : int, default True
            Number of iterations

        Returns
        -------
        __alpha : float
            calculated intercept
        __beta : float
            calculated slope
        """

        if len(x) != len(y):
            print("Dimension mismatch of x and y")
            return

        if learning_rate is not None:
            self.__learning_rate = learning_rate  # Learning rate
        self.__beta = beta or 0
        self.__alpha = alpha or 0

        while iterate:
            __beta_new = self.__beta - self.__learning_rate * ((-2/len(x))*sum((y-(self.__beta*x-self.__alpha))*x))
            __alpha_new = self.__alpha - self.__learning_rate * ((-2/len(x))*sum(y-self.__beta*x-self.__alpha))

            if iterate is True:
                # Break the loop when the coeffiecients are unchanged upto the first three decimals
                # When number of iterations are not provided.
                if np.round(__beta_new, 3) == np.round(self.__beta, 3) and np.round(__alpha_new, 3) == np.round(self.__alpha, 3):
                    break
            else:
                iterate = iterate - 1

            self.__beta = np.round(__beta_new, 3)
            self.__alpha = np.round(__alpha_new, 3)

        self.__beta = __beta_new
        self.__alpha = __alpha_new
        print("The Cost Function with the obtained parameters is", self.__cost_function(x, y))

        return self.__alpha, self.__beta

    def predict(self, x_new) -> float:
        """
        predict the label for a new observation
        Parameters
        ----------
        x_new : ndarray, list
            features of the test observation

        Returns
        -------
        y_hat : float
            predicted label
        """
        pass

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

if __name__ == "__main__":  # This code is for testing purpose
    n = int(input("Enter the np. of data points: "))
    reg = Gradent_descent()
    # x, y = input_data(n)
    x = np.array([23,26,30,34,43,48])
    y = np.array([651,762,856,1063,1190,1298])
    a, b = reg.fitting(x, y, 0.0001, 2000)
    yp = b*x + a
    print(len(yp))
    reg.plotting(x, y, yp)

    print("The regrssion function is: y = x*{} + {}".format(b, a))