class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def printList(self):
        temp = self.head
        while temp:
            print(str(temp.data)+" " ,end=" ")
            temp = temp.next
        
llist = LinkedList()
llist.insertAtBeginning(12)
llist.insertAtBeginning(11)
llist.insertAtBeginning(10)
llist.insertAtBeginning(9)
llist.insertAtBeginning(8)

llist.printList()