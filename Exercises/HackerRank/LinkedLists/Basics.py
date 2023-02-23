#-----------CREATING LINKED LIST---------------------
class Node:
    def __init__(self, datavalue=None):
        self.datavalue=datavalue
        self.nextNode=None
class FuncLinkedList:
    def __init__(self):
        self.head=None

    def traverseList(self):
        printval=self.head
        while printval is not None:
            print(printval.datavalue)
            printval=printval.nextNode

    def insertNodeAtTail(self, data):
        NewNode=Node(data)
        if self.head is None:
            self.head=NewNode
            return
        last=self.head
        while (last.nextNode):
            last=last.nextNode
        last.nextNode=NewNode
    def insertNodeAtHead(self, data):
        NewNode=Node(data)
        NewNode.nextNode=self.head
        self.head=NewNode
        

list=FuncLinkedList()
list.head = Node("A")
l2= Node("B")
l3= Node("C")
list.head.nextNode=l2
l2.nextNode=l3
list.insertNodeAtTail("Tail")
list.insertNodeAtHead('Head')

#-------------------------------------------------------

#---------------TRAVERSING-LINKED-LIST------------------
list.traverseList()

