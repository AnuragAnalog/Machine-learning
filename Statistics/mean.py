#!/usr/bin/python3

def mean(array: list) -> float:
    """
        Calculates the mean of a given array.
    """

    arr_sum = 0

    for element in array:
        arr_sum = arr_sum + element

    return arr_sum/len(array)

