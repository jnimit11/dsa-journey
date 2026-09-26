class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
def traverse(self):
    current = self.head
    if not current:
        print("Linked List is empty")
        return
    while current:
        print(current.data, end="-->")
        current = current.next
    print("None")
    
    
def insertAtfront(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
    
# LL = LinkedList()