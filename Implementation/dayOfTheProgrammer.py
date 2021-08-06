#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    if(year == 1918):
        return(f"26.09.{year}")
    if(1700 <= year <= 1917):
        if(year % 4 == 0): # Julian Leap Year
            return(f"12.09.{year}")
        else:
            return(f"13.09.{year}")
    else:    
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    return (f"12.09.{year}") # Gregorian Leap Year confirmed
                else:
                    return(f"13.09.{year}")
            else:
                return (f"12.09.{year}") # Gregorian Leap Year confirmed
        else:
            return(f"13.09.{year}")
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
