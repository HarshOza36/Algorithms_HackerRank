#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    l,r = 0,1
    while len(s) != 0:
        if(s[l] == s[r]):
            if(l == 0): 
                s = s[r+1:]
            else: 
                s = s[:l]+s[r+1:]
            l,r = 0,1
        else:
            if(r+1 == len(s)):
                break
            l += 1
            r += 1

    if(len(s) == 0):
        return  "Empty String"
    else:
        return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
