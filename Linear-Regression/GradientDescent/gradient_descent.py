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
    def __init__(self) -> None:
        self.__alpha = 0.0
        self.__beta = 0.0
        self.__learning_rate = 0.01

    def __str__(self) -> str:
        if self.__beta >= 0:
            return 'Regression Line\n'+str(self.__alpha)+' + '+str(self.__beta)+' x'
        else:
            return 'Regression Line\n'+str(self.__alpha)+str(self.__beta)+' x'

    def fitting(self, x: np.array, y: np.array, learning_rate: int =None) -> (float, float):
        """
            Computes the regression co-efficients for a simple linear regrssion
            by gradient descent method.
        """
        if len(x) != len(y):
            print("Dimension mismatch of x and y")
            return

        if learning_rate is not None:
            self.__learning_rate = None  # Learning rate
        self.__beta = 0
        self.__alpha = 0
        while True:
            __beta_new = self.__beta - self.__learning_rate * ((-2/len(x))*sum((y-self.__beta*x-self.__alpha)*x))
            __alpha_new = self.__alpha - self.__learning_rate * ((-2/len(x))*sum(y-self.__beta*x-self.__alpha))
            if np.round(__beta_new, 3) == np.round(self.__beta, 3) and np.round(__alpha_new, 3) == np.round(b, 3):
                self.__beta = __beta_new
                self.__alpha = __alpha_new
                break
            self.__beta = np.round(__beta_new, 3)
            self.__alpha = np.round(__alpha_new, 3)
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
        plt.scatter(yp, y-yp)

        plt.show()

if __name__ == "__main__":
    n = int(input("Enter the np. of data points: "))
    reg = Gradent_descent()
    # x, y = input_data(n)
    x = np.array([23,26,30,34,43,48])
    y = np.array([651,762,856,1063,1190,1298])
    a, b = reg.fitting(x, y, 0.01)
    yp = lambda x: b*x + a

    print("The regrssion function is: y = x*{} + {}".format(b, a))