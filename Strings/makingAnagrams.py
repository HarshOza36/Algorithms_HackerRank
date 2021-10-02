#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#
def get_freq(a):
    count = {} 
    for x in a:
        if(x in count):
            count[x] += 1
        else:
            count[x] = 1
    return count

def find_count(a, b):
    count = 0
    for ch in a:
        current = a[ch] - b.get(ch,0) 
        if current > 0:
            count += current
    return count
    
def makingAnagrams(s1, s2):
    # Write your code here
    
    freq_s1, freq_s2 = get_freq(s1), get_freq(s2)
    count = find_count(freq_s1,freq_s2) + find_count(freq_s2,freq_s1)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
