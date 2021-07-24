#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# def insertionSort(arr):
#     # Write your code here
#     len_arr = len(arr)
#     swaps = 0
#     if(len_arr <= 1):
#         return 0
#     else:
#         for i in range(1,len_arr):
#             j = i
#             while(j > 0 and arr[j] < arr[j-1]):
#                 arr[j], arr[j-1] = arr[j-1], arr[j]
#                 j -= 1
#                 swaps += 1
#     return swaps


# Insertion Sort being O(n^2) gave 6 Time Limit Exceeded cases
# Hence we will need O(nLogn) algorithm , So merge sort.
 
def mergeSort(arr):
    swaps = 0
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        swaps += mergeSort(left)
        swaps += mergeSort(right)
        i, j, k = 0, 0, 0
        len_left, len_right = len(left), len(right)
        while i<len_left and j<len_right:
            if left[i]<=right[j]:
                arr[k]=left[i]
                i=i+1
            else:
                arr[k]=right[j]
                j=j+1
                swaps += len_left-i
            k=k+1
        while i<len_left:
            arr[k]=left[i]
            i=i+1
            k=k+1
        while j<len_right:
            arr[k]=right[j]
            j=j+1
            k=k+1
    return swaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        # result = insertionSort(arr)
        try:
            result = mergeSort(arr)
        except Exception as e:
            result = -1

        fptr.write(str(result) + '\n')

    fptr.close()
