'''
You are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type float.
Print the reverse NumPy array with type float.
'''

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    b = numpy.array(arr,float)
    return b[::-1]
arr = input().strip().split(' ')
result = arrays(arr)
print(result)