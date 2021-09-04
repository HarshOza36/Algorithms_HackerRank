#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    
    rev_s = s[::-1]
    count = 0
    for i in range(1,len(s)):
        main_abs_diff = abs(ord(s[i-1]) - ord(s[i]))
        rev_abs_diff = abs(ord(rev_s[i-1]) - ord(rev_s[i]))
        if(main_abs_diff == rev_abs_diff):
            count += 1
    
    if(count == len(s)-1):
        return "Funny"
    else:
        return "Not Funny"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
