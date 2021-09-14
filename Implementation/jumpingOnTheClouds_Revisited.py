#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e = 100
    n = len(c)
    i = 0 
    loc = (i+k)%n
    while loc!=0:
        e -= 1
        if(c[loc] == 1):
            e -= 2
        i += k
        loc = (i+k)%n
    e -= 1 # Last step
    if(c[loc] == 1): # Checking if last step i.e. zero is thunderhead
        e -= 2
    return e

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
