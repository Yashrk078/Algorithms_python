'''
You are given two arrays: A and B.
Your task is to compute their inner and outer product.
'''
import numpy as np
import sys
#np.set_printoptions(legacy='1.13')

A = np.array([input().split()], int)
B = np.array([input().split()], int)
inner=np.inner(A,B)[0]
print(inner[0])
print(np.outer(A,B))
