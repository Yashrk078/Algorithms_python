# https://www.hackerrank.com/challenges/merge-the-tools/problem
def removeDuplicates(str):
    t = ""
    for i in str:
        if(i in t):
            pass
        else:
            t+=i 
    return t
def merge_the_tools(string, k):
    a = string
    split = len(string) // k
    start = 0
    while a != "":
        print(removeDuplicates(a[start:split]))
        a = a[split:]
        
print(merge_the_tools("AABCAAADA",2))