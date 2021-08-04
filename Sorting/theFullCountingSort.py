#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    final = []
    for i in range(len(arr)):
        if i < n//2:
            final.append((int(arr[i][0]),'-'))
        else:
            final.append((int(arr[i][0]),arr[i][1]))

    final.sort(key=lambda tup: tup[0]) 
    # print(final)
    print(*[x[1] for x in final])
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())
    countSort(arr)
