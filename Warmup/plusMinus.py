#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.


def plusMinus(arr, n):
    a = 0
    b = 0
    c = 0
    for i in range(0, n):
        if(arr[i] > 0):
            a = a+1
    print(a/n)
    for i in range(0, n):
        if(arr[i] < 0):
            b = b+1
    print(b/n)
    for i in range(0, n):
        if(arr[i] == 0):
            c = c+1
    print(c/n)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)
