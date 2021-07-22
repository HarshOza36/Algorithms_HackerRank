#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.


def miniMaxSum(arr):
    max = -sys.maxsize-1
    min = sys.maxsize
    sum = 0
    for x in arr:
        sum += x
        if x > max:
            max = x
        if x < min:
            min = x
    smin = sum-max
    smax = sum-min
    print(smin, smax)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
