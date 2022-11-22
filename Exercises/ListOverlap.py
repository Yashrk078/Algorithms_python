#Compare two randomly generated lists and return elements which occur in both lists
<<<<<<< Updated upstream
import random
def listOverlap(): 
    finalList = []
    listA = []
    listB = []
    sizeRangeA = random.randint(1,10)
    sizeRangeB = random.randint(1,10)    
    #Generating random values for listA
    for x in range(sizeRangeA):
        listA.append(int(random.randint(1,100)))
    #Generating random values for listA
    for x in range(sizeRangeB):
        listB.append(int(random.randint(1,100)))
    #Generating elements which occurred twice or more
=======

def listOverlap(listA, listB): 
    finalList = []
>>>>>>> Stashed changes
    for i in listA:
        for j in listB:
            if j == i:
                finalList.append(j)
            else:
                continue
<<<<<<< Updated upstream
    print(f'List A is :{listA}')
    print(f'List B is :{listB}')
    print(f'Occurences of Similar elements: {finalList}')

a = [1,2,3]
b = [1,5,6,7,3]
print(listOverlap())
=======
    return finalList

a = [1,2,3]
b = [1,5,6,7,3]
print(listOverlap(a,b))
>>>>>>> Stashed changes
