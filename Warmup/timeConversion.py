#!/bin/python3
import os
import sys


def timeConversion(s):
    a = s[0:2]
    if("AM" in s):
        if(s[0:2] == "12"):
            print("00"+s[2:8])
        else:
            print(s[0:8])
    elif("PM" in s):
        time = s.split(":")
        if(time[0] != "12"):
            time[0] = str(int(time[0])+12)
            ntime = ':'.join(time)
            b = str(ntime[:-2])
            print(b)
        else:
            print(s[0:8])


if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
