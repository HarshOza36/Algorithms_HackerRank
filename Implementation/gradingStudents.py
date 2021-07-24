#!/bin/python3
import os
import sys
def gradingStudents(grades,n):
    c=len(grades)
    for i in range(0,n):
        if(grades[i] >= 38):
            if(grades[i]+(5-grades[i]%5)-grades[i]<3):
                grades[i]=(grades[i]+(5-grades[i]%5))
                print(grades[i])
            else:
                print(grades[i])
        else:
             print(grades[i])
if __name__ == '__main__':
    n = int(input())
    grades = []
    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)
    result = gradingStudents(grades,n)
    
