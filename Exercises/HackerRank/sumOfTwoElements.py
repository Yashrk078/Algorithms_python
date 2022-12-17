"""
Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.

Example. m = 6 cost = [1,3,4,5,6]
The two flavors that cost 1 and 5 meet the criteria. Using 1-based indexing, they are at indices 1 and 4.
"""
arr = [1,4,5,3,2]
def sumOfTE(m, arr):
    for i in range(len(arr)):
        for _ in range(len(arr)):
            if i != _:
                if _ > i:
                    if arr[i]+arr[_]==m:
                        print(f"{i+1} {_+1}")
#                       return i+1, _+1

sumOfTE(4, arr)