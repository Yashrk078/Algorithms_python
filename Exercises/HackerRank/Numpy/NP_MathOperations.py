import numpy as np

N, _ = map(int, input().split())
A = np.array([input().split() for _ in range(N)], int)
B = np.array([input().split() for _ in range(N)], int)
print(A+B,A-B,A*B,np.floor_divide(A,B),A%B,A**B, sep="\n")
