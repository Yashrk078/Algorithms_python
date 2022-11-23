'''
You are given two integer arrays of size NXP and MXP (N & Mare rows, and P is
the column). Your task is to concatenate the arrays along axis 0.
'''
import numpy as np
import sys

N,M, P = map(int, input().split())
m1 = np.array([input().split() for _ in range(N)], int)
m2 = np.array([input().split() for _ in range(M)], int)
print(np.concatenate((m1, m2), axis =0))
