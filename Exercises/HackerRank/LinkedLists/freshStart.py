'''
Linked List: [None-->[head, nextNode]-->[data, NextNode]-->[data, nextNode]-->None]

class Node:
    which will contain :
        data :  to hold data
        nextNode : to point to next node (this will be instance object of next Node)

class LinkedList:
    start Head value with None:
    __init__():
        head = None
'''
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        self.head=None
    
    def insertAtTail(self, data) :
        newNode = Node(data)
        if self.head is None:
            self.head=newNode
        curNode = self.head
        while curNode.next is not None:
            curNode = curNode.next
        curNode.next = newNode

    def insertAtHead(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def insertAtMid(self, curNode, data):
        newNode = Node(data)
        self.curNode = curNode
        newNode.next = curNode.next
        curNode.next = newNode
    
def traverseList(head):
    curnode=head
    while curnode !=None:
        print(curnode.data)
        curnode = curnode.next


a = Node('A')
b = Node('B')
c = Node('C')
llist= LinkedList()
llist.head = a
a.next = b
b.next = c
llist.insertAtTail('TAIL')
llist.insertAtHead('HEAD')
llist.insertAtMid(b, 'MID')
traverseList(llist.head)
