"""
Given a square matrix, calculate the 
absolute difference between the sums of its diagonals.
"""
import numpy as np
a = [[11, 2, 4],
[4, 5, 6],
[10, 8, -12]]

def method1(arr):
    d1 = np.flip(a).diagonal()
    d2 = np.fliplr(a).diagonal()
    sum1=sum(d1)
    sum2=sum(d2)
    print("Diagonal 1:",d1)
    print("Diagonal 2:",d2)
    return (abs(sum1-sum2))

def method2(arr):
    # Without using numpy
    len_arr=len(arr)
    x_left, y_left = 0, 0
    x_right, y_right = len_arr-1, 0

    d1, d2 = 0, 0
    for _ in range(len_arr):
        d1 += arr[y_left][x_left]
        d2 += arr[y_right][x_right]
        x_left += 1
        y_left += 1
        y_right +=1
        x_right -= 1
    return abs(d1 - d2)