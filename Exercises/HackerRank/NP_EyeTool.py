'''
Your task is to print an array of size NXM
with its main diagonal elements as 1's and 0's everywhere else.

Eye tool is used to create a matrix with diagonal.
 k = 0 : main diagonal
 k = 1..n : upper diagonal
 k = -1..n: lower diagonal
'''

import numpy as np
np.set_printoptions(legacy='1.13')
import sys

N,M = map(int, input().split())
m = np.eye(N, M, k = 0)
print(m)
