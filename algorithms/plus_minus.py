#!/bin/python3

import sys

def plusMinus(arr):
    # Complete this function
    plus = 0
    minus = 0
    zero = 0
    for i in range(n):
        if arr[i] > 0:
            plus += 1
        elif arr[i] < 0:
            minus += 1
        else:
            zero += 1
            
    print(round(plus/len(arr), 6))
    print(round(minus/len(arr), 6))
    print(round(zero/len(arr), 6))
    # end of my code
    
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)