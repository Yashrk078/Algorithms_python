'''
https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true
'''

def aplOrnge(s, t, a, b, apples, oranges):
    posApple = []
    posOrange = []
    result = []
    a_count=0
    b_count=0
    print(f'apples{apples}, ornages:{oranges}, a:{a}, b:{b}')
    for i in apples: posApple.append(i+a)
    print(posApple)
    for j in oranges: posOrange.append(j+b)
    print(posOrange)
    for x in posApple: 
        if x >= s and x <=t:
            a_count+=1
    for y in posOrange:
        if y >=s and y <= t:
            b_count+=1
    print(a_count)
    print(b_count)

aplOrnge(7, 11, 5, 15, [-2, 2, 1], [5, -6])
