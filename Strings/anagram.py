#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def get_freq(a):
    count = {} 
    for x in a:
        if(x in count):
            count[x] += 1
        else:
            count[x] = 1
    return count

def anagram(s):
    # Write your code here
   
    if(len(s) % 2 != 0):
        return -1
    
    n = len(s)//2
    a = s[:n]
    b = s[n:]
    count = 0
    s1,s2 = get_freq(a),get_freq(b)
            
    for ch in s2:
        current = s2[ch] - s1.get(ch,0) 
        # we use get dict method so if we have ch in a we will get its frequency else 0
        if current > 0:
            count += current
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
