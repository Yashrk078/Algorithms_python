highest=0
runnerup=0
#Condition print runnerUp such as:
# highest < runnerUp < others

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    #Method 1
    # if n>=2 and n<=100:
    #     for i in range(n):
    #         if arr[i]>=-100 and arr[i]<=100:
    #             for _ in range(len(arr)):
    #                 if arr[_] > highest:
    #                     highest=arr[_]
    #             for _ in range(len(arr)):
    #                 if arr[_] > runnerup:
    #                     if arr[_] < highest:
    #                         runnerup=arr[_]
    #     print(runnerup)
    
    #Method 2
    list1=list(set(arr))
    list1.sort()
    print(list1[-2])