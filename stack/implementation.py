# Simple stack implementation using a Python list.
# This stack follows LIFO (Last In, First Out) behavior.
class Stack:
    def __init__(self):
        # Store stack elements in a list.
        self.s = []

    # Return the current number of items in the stack.
    def length(self):
        return len(self.s)

    # Add an item to the top of the stack.
    def push(self, value):
        self.s.insert(0, value)

    # Return the top item without removing it.
    def peek(self):
        if len(self.s) == 0:
            raise Exception("stack is empty")
        else:
            return self.s[0]

    # Remove and return the top item from the stack.
    def pop(self):
        if len(self.s) == 0:
            raise Exception("stack is empty")
        else:
            return self.s.pop(0)

# Create a stack object.
stk = Stack()

# Push some values onto the stack.
stk.push(10)
stk.push(20)
stk.push(30)

# Uncomment the next line to view the top element without removing it.
# print(stk.peek())

# Pop and print items from the stack in LIFO order.
print(stk.pop())
print(stk.pop())
print(stk.pop())