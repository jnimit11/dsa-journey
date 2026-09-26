class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)
        
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
            
        temp.next = new_node
        
    def printList(self):
        temp = self.head
        while temp:
            print(str(temp.data)+" " ,end=" ")
            temp = temp.next
        
llist = LinkedList()
llist.insertAtEnd(12)
llist.insertAtEnd(11)
llist.insertAtEnd(10)
llist.insertAtEnd(9)
llist.insertAtEnd(8)

llist.printList()