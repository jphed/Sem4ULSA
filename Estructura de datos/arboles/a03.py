class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val),
        printInorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val),

def printPreorder(root):
    if root:
        print(root.val),
        printPreorder(root.left)
        printPreorder(root.right)

# Crear el árbol binario
root = Node('r')
root.left = Node('a')
root.right = Node('b')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.left = Node('f')
root.right.right = Node('g')

print("Recorrido Preorden (Raíz-Izquierda-Derecha):")
printPreorder(root)

print("\nRecorrido Inorden (Izquierda-Raíz-Derecha):")
printInorder(root)

print("\nRecorrido Postorden (Izquierda-Derecha-Raíz):")
printPostorder(root)