#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here
    if(s[::-1] == s):
        return -1
    else:
        # Below is O(n) time , which gives 3 TLE
        # for i in range(len(s)):
        #     new = s[:i] + s[i+1:]
        #     if(new[::-1] == new):
        #         return i
    
        # Optimizing the solution by checking only first half
        for i in range(len(s)//2):
            if(s[i] != s[-(i+1)]):
                new = s[:i] + s[i+1:] 
                if(new[::-1] == new):
                    return i
                return -(i+1) + len(s)
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
