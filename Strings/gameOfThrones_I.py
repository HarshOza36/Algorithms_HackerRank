#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    # Write your code here
    freq = {}
    for ch in s:
        if(ch in freq):
            freq[ch] += 1
        else:
            freq[ch] = 1
    ans = 0 
    for i in freq.values():
        ans += i % 2
    return "NO" if(ans > 1) else "YES" 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
