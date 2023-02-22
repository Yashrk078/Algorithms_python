'''
https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
'''
def permute(x, y, z, n):
    f_list= [[i,j,k] for i in [a for a in range(0, x+1)] for j in [b for b in range(0, y+1)] for k in [c for c in range(0,z+1)] if i+j+k != n]
    #print(f_list)
    return f_list
permute(1,1,2,3)
