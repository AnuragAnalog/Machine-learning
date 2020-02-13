# Machine Learning

## Prerequsities

* Probability

* Statistics

* Linear Algebra

* Calculus

To get a basic understanding on the statistics, you can try [this](https://www.hackerrank.com/domains/tutorials/10-days-of-statistics) course in HackerRank.

And, [here](https://github.com/AnuragAnalog/hackerrank/tree/master/tutorial-10-days-of-statistics) is the solutions.

## Datasets

* Random Dataset for Linear regression

## Loss functions

### Mean Squared Error(MSE)
It is the average squared error between the actual and the predicted observations, it is also called as Quadratic Loss, L2 Loss.
This method penalizes the values which have high error.

### Mean Absolute Error(MAE)
It is the average absolute error between the actual and the predicted observations, it is also called as L1 Loss
This method is more sensitive to outliers than MSE, this also needs more complex techniques to compute the gradients.

### Mean Bais Error
It is just the difference between the actual and the predicted value, we should take a bit care when dealing with positive and negative bais, because they can make the total bais less.