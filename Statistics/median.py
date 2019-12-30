#!/usr/bin/python3

def median(array: list) -> float:
    """
        Calculates the median of a given array.
    """

    tmp_arr = sorted(array)

    if len(array)%2 == 1:
        median = tmp_arr[int(n//2)]
    else:
        median = (tmp_arr[int(n//2)]+tmparr[int(n//2)-1])/2

    return median
