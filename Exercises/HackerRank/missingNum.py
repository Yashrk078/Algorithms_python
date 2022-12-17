#https://www.hackerrank.com/challenges/missing-numbers/problem?isFullScreen=true
# {under-construction}

a = [7,2,5,3,5,3]
b = [7,2,5,4,6,3,5,3]

def missingNum(arr, brr):
    for i in range(len(brr)):
        if brr[i] in arr:
            pass
            print(brr[i], end=" ")

missingNum(a,b)
