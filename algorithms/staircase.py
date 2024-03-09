#!/bin/python3

import os
import sys

#
# Complete the staircase function below.
#
def staircase(n):
    #
    # Write your code here.
    #
    for i in range(n):
        stair = (i + 1) * "#"
        print(stair.rjust(n))
    # end of my code

if __name__ == '__main__':
    n = int(input())

    staircase(n)