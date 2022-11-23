'''
Without using any string methods, try to print the following:

Note that "

" represents the consecutive values in between.

Example
Print the string .
'''
if __name__ == '__main__':
    n = int(input())
    for i in range(n+1):
        if i == 0:
            continue
        else:
            print(i,end="")