import numpy as np

N, M = map(int, input().split())
m = np.zeros((N, M), dtype=int)
for i in range(N):
    m[i] = np.array(input().split())

print(m.transpose())
print(m.flatten())
