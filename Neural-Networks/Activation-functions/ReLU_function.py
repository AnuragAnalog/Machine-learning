
from math import exp

def sigmoid(a: float) -> float:
    """
        Rectified Linear Unit(ReLU), which has a ramp shape, it defines the
        positive part of the argument.
    """

    return max(0, a)