'''
You are given two arrays and . Both have dimensions of NXM.
Your task is to compute their matrix product.
'''
import numpy as np
import sys

N = int(input())
A = np.array([input().split() for i in range(N)], int)
B = np.array([input().split() for i in range(N)], int)
print(np.dot(A,B))
