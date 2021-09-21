#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    # Using the maths concept 
    # a+b is divisible by k iff (a % k) + (b % k) = k
    
    # getting the remainder counts
    counts = [0] * k
    for no in s:
        counts[no % k] += 1

    cnt = min(counts[0], 1)
    for i in range(1, (k//2)+1):
        if(i != k-i): # to remove the condition where say if k = 4, therefore pair of counts[2] will also be counts[2](i=2 then, k-i = 2)
            cnt += max(counts[i], counts[k-i])
    if(k%2 == 0):
        cnt += 1

    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
