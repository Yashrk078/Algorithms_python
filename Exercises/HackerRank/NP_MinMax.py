#https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true
import numpy as np
import sys

N, _ = map(int, input().split())
A = np.array([input().split for _ in range(N)], int)
minimum = np.min(A, axis = 1)
print(np.min(minimum))
