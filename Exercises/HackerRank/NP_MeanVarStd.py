'''
You are given a 2-D array of size NXM
.
Your task is to find:

The mean along axis 1
The var along axis 0
The std along axis None
'''

import numpy as np
import sys
#np.set_printoptions(legacy='1.13')
N, _ = map(int, input().split())
A = np.array([list(map(int, input().split())) for _ in range(N)] ,int)
print(np.mean(A, axis = 1))
print(np.var(A, axis = 0))
print(round(np.std(A,axis=None),11))
