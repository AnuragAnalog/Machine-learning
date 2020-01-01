#!/usr/bin/python3

import median    #From the current directory import medain module

def quartile(arr: list) -> (float, float, float):

    q2 = median.median(arr)
    n = len(array)

    if n%2 == 1:
        tmp = arr[:int(n//2)]
        q1 = median.median(tmp, len(tmp))
        tmp = arr[int(n//2)+1:]
        q3 = median.median(tmp, len(tmp))
    else:
        tmp = arr[:int(n//2)]
        q1 = median.median(tmp, len(tmp))
        tmp = arr[int(n//2):]
        q3 = median.median(tmp, len(tmp))

    return q1, q2, q3
