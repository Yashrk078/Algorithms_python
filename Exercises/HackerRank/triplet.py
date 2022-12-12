"""
The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].

    If a[i] > b[i], then Alice is awarded 1 point.
    If a[i] < b[i], then Bob is awarded 1 point.
    If a[i] = b[i], then neither person receives a point.

"""
a=[1,2,3]
b=[3,2,1]
def triplet(a,b):
    alice=0
    bob=0
    if len(a)==len(b):
        for i in range(len(a)):
            if a[i]>b[i]:
                alice+=1
            elif a[i]<b[i]:
                bob+=1
            else:
                pass
    return [alice, bob] 
print(triplet(a,b))