def binsrch(arr, target) -> int:
    h = len(arr)-1
    l = 0
    if h >= l:
        m = (h+l) // 2
        if arr[m]==target:
            return m
        elif arr[m] < target:
            print(f'm:h{arr[m:]}')
            return binsrch(arr[m:], target)
        else:
            print(f'l:m{arr[:m]}')
            return binsrch(arr[:m], target)
print(binsrch([1,2,3,4,5,6,7,8], 2))
