class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def inOrder(root):
    if root:
        
        inOrder(root.left)
        print(str(root.data)+ " ", end='')
        inOrder(root.right)

def preOrder(root):
    if root:
        print(str(root.data)+ " ", end='')
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(str(root.data)+ " ", end='')

# driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Inorder traversal")
inOrder(root)
print()
print("preOrder traversal")
preOrder(root)
print()
print("postOrder traversal")
postOrder(root)