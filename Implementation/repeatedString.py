#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    # Brute force, TLE
    # count = 0
    # len_s = len(s)
    # for i in range(n):
    #     if(s[i%len_s] == "a"):
    #         count += 1
    # return count
    count_a = s.count("a")
    len_s = len(s)
    # counting the frequency of s in infinite string
    s_freq = n//len(s)
    remaining_s_count = 0
    if(len_s*s_freq != n):
        diff = n - (len_s*s_freq)
        remaining_s_count = s[:diff].count("a")
        
    return int(count_a * s_freq) + remaining_s_count
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
