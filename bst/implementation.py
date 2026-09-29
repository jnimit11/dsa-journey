class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
def insertBST(root, key):
        if root is None:
            return Node(key)
        else:
            if root.data == key:
                return root
            elif root.data < key:
                root.right = insertBST(root.right, key)
            else:
                root.left = insertBST(root.left, key)
        return root
    
def inOrder(root):
    if root:
        inOrder(root.left)
        print(str(root.data)+ " ", end='')
        inOrder(root.right)

# searching in BST
def searchBST(root, key):
    if root is None or root.data == key:
        return root
    elif key < root.data:
        return searchBST(root.left, key)
    else:
        return searchBST(root.right, key)

root = Node(100)
root = insertBST(root, 80)
root = insertBST(root, 110)
root = insertBST(root, 50)
root = insertBST(root, 90)

print("Inorder traversal")
inOrder(root)

key = 40
result = searchBST(root, key)
print()
if result:
    print("data is present in BST")
else:
    print("data is not present in BST")