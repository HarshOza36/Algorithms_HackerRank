#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    encryted = ""
    for ch in s:
        if(ch.isalpha()):
            if(ch.isupper()):
                encryted += chr((ord(ch) + k - 65) % 26 + 65)
            else:
                encryted += chr((ord(ch) + k - 97) % 26 + 97)
        else:
            encryted += ch
            
    return encryted
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()