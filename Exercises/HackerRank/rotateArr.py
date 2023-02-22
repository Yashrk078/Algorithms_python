'''
https://www.hackerrank.com/challenges/array-left-rotation/problem?isFullScreen=true
'''

def rotateLeft(arr, t):
    print(f'original array: {arr}')
    for i in range(t):
        arr.append(arr[0])
        arr.pop(0)
    return arr

print(rotateLeft([2,4,2,3,2,3],3))