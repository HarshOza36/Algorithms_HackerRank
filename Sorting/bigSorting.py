#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

def bigSorting(unsorted):
    # Below code is correct but time limit exceeded
    # Also i used map here to convert to int and back to string which increases time.
    # sorted_arr = sorted(list(map(int,unsorted)))
    # sorted_arr = list(map(str,sorted_arr))
    # return sorted_arr
    
    # return sorted(unsorted,key=int)

    # lets try using sort method
    # unsorted.sort(key=int)
    # return unsorted
    
    # unfortunately sort() method also converts internally  int->str and str->int so 
    # its slow
    # I implemented merge sort,quicksort still time limit exceeds =(
    
    # In python the sort function starts comparing the string from ASCII value of most significant digits. Hence the most significant bits(MSB) are sorted here.
    # list of strings, specifying key=len (the built in len() function) sorts the strings by length, from shortest to longest. Since MSBs are sorted, now by length
    # we can sort instantly. Check example below
    #>>> a = ['100','20','9','2','3','10','99']
    #>>> a.sort()
    #>>> a
    #['10', '100', '2', '20', '3', '9', '99']
    #>>> sorted(a,key=len)
    #['2', '3', '9', '10', '20', '99', '100']

    unsorted.sort()
    return sorted(unsorted,key=len)
    # This runs instantly
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
