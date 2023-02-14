class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

    def set_left(self, left):
        self.left = left
    
    def set_right(self, right):
        self.right = right

    def preorder(self):
        print(self.name, end = "")
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()
        return

    def inorder(self):
        if self.left != None:
            self.left.inorder()
        print(self.name, end = "")
        if self.right != None:
            self.right.inorder()
        return

    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print(self.name, end = "")
        return    

n = int(input())
nodes = []
for i in range(n):
    name = chr(ord('A') + i)
    nodes.append(Node(name))

for i in range(n):
    a, b, c = input().split()
    if b != ".": nodes[ord(a) - ord("A")].set_left(nodes[ord(b) - ord("A")])
    if c != ".": nodes[ord(a) - ord("A")].set_right(nodes[ord(c) - ord("A")])

nodes[0].preorder()
print()
nodes[0].inorder()
print()
nodes[0].postorder()
print()
