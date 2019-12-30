#!/usr/bin/python3

def mode(array: list) -> float:
    """
        Calculates the mode of a given array, if two or more elements have the highest frequency then mode is the smallest value among them.
    """

    if len(set(array)) == len(array):
        mode = min(array)
    else:
        maxi = 0
        val = []
        for e in set(arr):
            # Comapring frequency's of current element and mode
            if arr.count(e) > maxi:
                maxi = arr.count(e)
                val = e
            elif arr.count(e) == maxi:
                if val > e:
                    val = e
        mode = val

    return mode
