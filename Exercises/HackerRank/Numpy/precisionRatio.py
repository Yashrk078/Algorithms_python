"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
 Print the decimal value of each fraction on a new line with places after the decimal.
"""

arr=[-4, 3, -9, 0, 4, 1]
def plusMinus(arr):
    l=len(arr)
    pos=0
    neg=0
    zero=0
    for _ in range(len(arr)):
        if arr[_] > 0:
            pos+=1
        elif arr[_]<0:
            neg+=1
        else:
            zero+=1
    return ("{:.6f}".format(pos/l)+"\n"+"{:.6f}".format(neg/l)+"\n"+"{:.6f}".format(zero/l))

print(plusMinus(arr))