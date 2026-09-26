class Deque:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def inserAtEnd(self, value):
        self.items.append(value)
        
    def deleteAtFront(self):
        if self.isEmpty():
            print("queue is empty")
        return self.items.pop(0)
    
    def insertAtbeginning(self, value):
        self.items.insert(0, value)
        
    def deleteAtEnd(self):
        self.items.pop()
        
dq = Deque()
dq.inserAtEnd(10)
dq.insertAtbeginning(20)
dq.inserAtEnd(30)
dq.inserAtEnd(40)
dq.insertAtbeginning(50)
