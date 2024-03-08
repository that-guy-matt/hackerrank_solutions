#!/bin/python3

import sys

def aVeryBigSum(n, ar):
    # Complete this function
    total = 0
    for i in range(n):
        total += ar[i]
    return total
    # End my code

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)