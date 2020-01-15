
from math import exp

def sigmoid(z: float) -> float:
    """
        It's a mathematical function, which has a characterstic
        S-shaped curve, it's also known as logistic function.
    """

    return 1/(1+exp(-1*z))