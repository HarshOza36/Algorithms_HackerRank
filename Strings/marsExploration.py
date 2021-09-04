#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    count = 0
    for i,ch in enumerate(s):
        if(i % 3 == 0 and ch != "S"):
            count += 1
        if(i % 3 == 1 and ch != "O"):
            count += 1
        if(i % 3 == 2 and ch != "S"):
            count += 1  
    return count  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
