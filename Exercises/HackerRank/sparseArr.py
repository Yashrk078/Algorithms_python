'''
https://www.hackerrank.com/challenges/sparse-arrays/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
'''
strList = ['ab','ab','abc', 'ab']
qryList = ['ab', 'abc','bc']

def matchStrs(strlst, qrylst):
    counterLst= []
    count=0
    for i in qryList:
        for j in strList:
            if i==j:
                count+=1
        counterLst.append(count)
        count=0
    return counterLst

print(matchStrs(strList, qryList))
