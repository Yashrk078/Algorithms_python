#Compare two randomly generated lists and return elements which occur in both lists

def listOverlap(listA, listB): 
    finalList = []
    for i in listA:
        for j in listB:
            if j == i:
                finalList.append(j)
            else:
                continue
    return finalList

a = [1,2,3]
b = [1,5,6,7,3]
print(listOverlap(a,b))