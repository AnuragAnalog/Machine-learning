#!/usr/bin/python3

"""
    ### Multiple Linear Regression ###
    Computes the regression coefficients using the gradient descent method
"""

import numpy as np
import pandas as pd

class Gradent_descent():
    """
    Fit a linear model with n features using gradient descent
    """

    def __init__(self) -> None:
        self.__coef = list()
        self.__learning_rate = 0.01
        self.__lambda = 0.0

    def __str__(self) -> str:
        return "Reg coef"+str(self.__coef)

    def __cost_function(self, x: np.array, y: np.array) -> float:
        # Calculates the cost of the given regression line.

        if len(x) != len(y):
            print("Dimension mismatch of x and y")
            return

        J = 0
        tmp_x = np.append(x, np.ones((self.data_length, 1)), axis=1)
        tmp_x = tmp_x * self.__coef
        J = np.sum(tmp_x, axis=1)
        J = np.sum(J)/len(x)

        return J

    def get_params(self):
        """
        Returns
        -------
        coef : ndarray
            returns an 1-d array of coefficients
        """

        return self.__coef

    def fitting(self, x: np.array, y: np.array, learning_rate: float =None, iterate: int =True) -> (float, float):
        """
        Fit a linear model

        Parameters
        ----------
        x : ndarray, list
            A 1-d array which represents features array of the data
        y : ndarray, list
            A 1-d array which represents labels of the data
        learning_rate : float, default None
            Learning rate for the convergence
        iterate : int, default True
            Number of iterations

        Returns
        -------
        __coef : ndarray
            Calculated Coefficients
        """

        if len(x) != len(y):
            print("Dimension mismatch of x and y")
            return

        self.data_length = len(x)
        self.features = x.shape[1]
        self.__coef = np.zeros((self.features+1, 1))

        __coef_new = np.empty_like(self.__coef)
        train_x = np.append(x, np.ones((self.data_length, 1)), axis=1)

        if learning_rate is not None:
            self.__learning_rate = learning_rate  # Learning rate

        while iterate:
            print(self.__coef)
            for j in range(self.features+1):
                tmp_grad = 0
                for i in range(self.data_length):
                    tmp_grad = ((y[i] - np.sum(train_x[i] * self.__coef)) * train_x[i][j])/self.data_length
                __coef_new[j] = self.__coef[j] - self.__learning_rate * tmp_grad
            # __coef_new = self.__coef - self.__learning_rate * ((-2/self.data_length)*np.sum((y - np.sum((train_x * self.__coef), axis=1).reshape(self.data_length, -1))*train_x))

            if iterate is True:
                # Break the loop when the coeffiecients are unchanged upto the first three decimals
                # When number of iterations are not provided.
                if all(np.round(__coef_new, 3) == np.round(self.__coef, 3)):
                    break
            else:
                iterate = iterate - 1

            self.__coef = np.round(__coef_new, 3)

        self.__coef = __coef_new
        print("The Cost Function with the obtained parameters is", self.__cost_function(x, y))

        return self.__coef

    def predict(self, x_new) -> float:
        """
        Predict the label for a new observation

        Parameters
        ----------
        x_new : ndarray, list
            features of the test observation

        Returns
        -------
        y_hat : float
            predicted label
        """

        tmp_x = np.append(x_new, [1], axis=1)
        y_hat = tmp_x * self.__coef

        return y_hat

if __name__ == "__main__":  # This code is for testing purpose
    n = int(input("Enter the np. of data points: "))
    data = pd.read_csv('../dataset.csv')
    y = data[['price']].values
    data.drop(['price'], axis=1, inplace=True)
    x = data.values
    reg = Gradent_descent()
    print(reg.fitting(x, y, 0.0001, 20))
