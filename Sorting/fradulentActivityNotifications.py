#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#
# Brute Force - Many TLE
    # notifs = 0
    # for i in range(len(expenditure)-d):
    #     arr = sorted(expenditure[i:d+i])
    #     mid = len(arr)//2
        
    #     if(len(arr)%2!=0): 
    #         median = arr[mid]
    #     else:
    #         median = (arr[mid]+arr[mid-1])/2
        
    #     if(expenditure[d+i] >= (2*median)):
    #         notifs += 1
    # return notifs
def activityNotifications(expenditure, d):
    # Write your code here
    
    freq = {}
    def get_median(idx):
        s = 0
        for i in range(201): # since range of expenditure is 0-200
            temp = 0
            if(i in freq):
                temp = freq[i]
            s += temp
            if(s >= idx):
                return i
            
    result = 0
    for i in range(n):
        val = expenditure[i]
        if(i >= d):
            med = get_median(d//2 + d%2)
            if(d % 2 == 0):
                if(val >= med + get_median(d//2+1)):
                    result += 1
            else:
                if(val >= med*2):
                    result += 1
                    
        if(val in freq):
            freq[val] += 1
        else:
            freq[val] = 1
        if(i >= d):
            prev = expenditure[i-d]
            freq[prev] -= 1
            
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
