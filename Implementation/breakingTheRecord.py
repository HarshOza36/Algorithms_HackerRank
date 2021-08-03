#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    min_rec, max_rec = scores[0],scores[0]
    min_rec_count, max_rec_count = 0,0
    
    for i in range(1,len(scores)):
        temp_min_rec = min(min_rec,scores[i])
        temp_max_rec = max(max_rec,scores[i])
        
        if(temp_min_rec <  min_rec):
            min_rec_count += 1
            min_rec = temp_min_rec
        if(temp_max_rec > max_rec):
            max_rec_count += 1
            max_rec = temp_max_rec
            
    return [max_rec_count,min_rec_count]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
