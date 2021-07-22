#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.


def birthdayCakeCandles(ar, ar_count):
    a = max(ar)
    count = 0
    for i in range(0, ar_count):
        if(a == ar[i]):
            count = count+1
    return(count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(ar, ar_count)
    fptr.write(str(result) + '\n')
    fptr.close()
