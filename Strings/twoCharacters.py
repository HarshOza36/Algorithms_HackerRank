#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    # Write your code here
    set_s = list(set(s))
    if len(set_s)<2:
        return 0
    
    # forming combinations
    two_combinations = []
    for i in range(len(set_s)):
        for j in range(i+1,len(set_s)):
            two_combinations.append({set_s[i],set_s[j]})
    
    
    m = 0
    for com in two_combinations:
        others = set(s) - com # elements other than combinations
        temp = s
        for j in others: # for removing other elements and keeping combinations
            temp = temp.replace(j,"")
        
        # forming final alternating string 
        alt = ("".join(com))*(len(temp)//2)
        if alt+alt[0] == temp or alt == temp or alt == temp[::-1] or alt[1]+alt == temp:
            # for ab combination if alt is abab then our alternative string can be
            # ababa, abab, palindrome , babab
            m = max(m,len(temp))
    return m
    
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
