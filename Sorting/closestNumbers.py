#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    difference = []
    arr.sort()
    m = float('inf')
    for i in range(len(arr)-1):   
        m = min(abs(arr[i+1]-arr[i]),m)  
    print(m)
    # we Found the minimum difference now lets compare the values
    for i in range(len(arr)-1): 
        if abs(arr[i+1]-arr[i]) == m:
            difference.append(arr[i])
            difference.append(arr[i+1])
    return difference

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
