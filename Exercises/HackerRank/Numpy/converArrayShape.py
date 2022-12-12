import numpy as np

def convertShape(arr):
    arr = np.array(arr, dtype = np.int8)
    return np.array(arr).reshape(3,3)
    

if __name__ == '__main__':
    n = input().strip().split(' ')
    print(convertShape(n))
