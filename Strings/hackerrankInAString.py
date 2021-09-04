#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def hackerrankInString(s):
    # Write your code here
    h = "hackerrank"
    k = 0
    for i in range(len(h)):
        flag = False
        for j in range(k,len(s)):
            if(s[j] == h[i]):
                k = j+1
                flag = True
                break
        if(flag == False):
            return "NO"
    return "YES"
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
