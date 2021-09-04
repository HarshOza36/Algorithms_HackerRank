#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    if(s[0] == "0" or len(s) <= 1):
        print("NO")
        return
    else:
        check = True
        for i in range(1,len(s)//2+1):
            n = int(s[:i])
            temp = []
            for j in range(len(s)//i):
                temp.append(str(n+j))
            
            if(''.join(temp)[:len(s)] == s):
                print("YES "+str(n))
                check = False
                break
        if check:            
            print('NO')
                 
    

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
