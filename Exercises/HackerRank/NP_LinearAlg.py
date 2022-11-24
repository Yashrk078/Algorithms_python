'''
You are given a square matrix with dimensions NXN.
Your task is to find the determinant.
Note: Round the answer to 2 places after the decimal.
'''

#https://numpy.org/doc/stable/reference/routines.linalg.html

import numpy as np
import sys

N = int(input())
A = np.array([input().split() for _ in range(N)], float)
print(round(np.linalg.det(A),2))


'''
OTHER LINEAR ALGEBRAIC OPERATIONS:

linalg.det

The linalg.det tool computes the determinant of an array.

print numpy.linalg.det([[1 , 2], [2, 1]])       #Output : -3.0

linalg.eig

The linalg.eig computes the eigenvalues and right eigenvectors of a square array.

vals, vecs = numpy.linalg.eig([[1 , 2], [2, 1]])
print vals                                      #Output : [ 3. -1.]
print vecs                                      #Output : [[ 0.70710678 -0.70710678]
                                                #          [ 0.70710678  0.70710678]]

linalg.inv

The linalg.inv tool computes the (multiplicative) inverse of a matrix.

print numpy.linalg.inv([[1 , 2], [2, 1]])       #Output : [[-0.33333333  0.66666667]
                                                #          [ 0.66666667 -0.33333333]]

'''
