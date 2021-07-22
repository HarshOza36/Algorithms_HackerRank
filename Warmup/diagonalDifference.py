#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.


def diagonalDifference(arr, n):
    a = 0
    b = 0
    leng = len(arr)
    for i in range(0, n):
        a = a+arr[i][i]
        b = b+arr[leng-1-i][i]
    return(abs(a-b))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()
