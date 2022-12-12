#https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true
'''
You are given a 2-D array with dimensions N x M.
Your task is to perform the min function over axis 1 and then find the max of that.
'''

import numpy as np
import sys
np.set_printoptions(legacy="1.13")
N, _ = list(map(int, input().split()))
A = np.array([list(map(int, input().split())) for _ in range(N)], int)
print(np.min(A, axis=1).max())
