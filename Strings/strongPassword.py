#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    specials = "!@#$%^&*()-+"
    # format of arr [num,up,low,special]
    arr = [False,False,False,False]
    for ch in password:
        if(ch.isdigit()):
            arr[0] = True
        if(ch.isupper()):
            arr[1] = True
        if(ch.islower()):
            arr[2] = True
        if(ch in specials):
            arr[3] = True
    count = 0
    if(n < 6): 
        count += max(6-n,arr.count(False))
    else:
        count += arr.count(False)
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()