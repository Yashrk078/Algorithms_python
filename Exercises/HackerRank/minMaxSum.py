"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print 
the respective minimum and maximum values as a single line of two space-separated long integers. 
"""

arr=[1,2,3,4,5]

def arrSum(arr):
    total=0
    minMax = []
    for i in range(len(arr)):
        total=sum(arr)
#        print((total)-arr[i])
        minMax.append((total)-arr[i])
    return minMax

minMax=arrSum(arr)
print(min(minMax), end=" ")
print(max(minMax))
# print(sum(arr[1:]))
# print(sum((arr[:len(arr)-1])))
    

