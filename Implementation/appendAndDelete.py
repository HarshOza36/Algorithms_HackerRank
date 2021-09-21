#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    sameChars = min(len(s), len(t))
    for i in range(len(t)):
        if s[:i] != t[:i]:
            sameChars = i-1
            break

    diff = (len(s) - sameChars) + (len(t)- sameChars)
    if (diff <= k and diff % 2 == k % 2) or (len(s) + len(t) < k) : 
        return "Yes"
    else:
        return "No"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
