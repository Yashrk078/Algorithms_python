'''
You are given a 2-D array with dimensions NXM.
Your task is to perform the sum tool over axis 0 and then find the product
of that result.
'''

import numpy as np
import sys

N, _ = map(int, input().split())
A = np.array([input().split() for _ in range(N)], int)
addition = np.sum(A, axis=0)
print(np.prod(addition, axis = None))
