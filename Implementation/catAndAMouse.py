#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    cat_a_loc = abs(z-x)
    cat_b_loc = abs(z-y)
    if(cat_a_loc == cat_b_loc):
        return ("Mouse C")
    elif(cat_a_loc < cat_b_loc):
        return ("Cat A")
    else:
        return ("Cat B")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
