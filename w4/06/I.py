import sys

sys.setrecursionlimit = 10000
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        curr = self
        while True:
            if value < curr.value:
                if curr.left is None:
                    curr.left = BST(value)
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = BST(value)
                    break
                curr = curr.right

data_input = sys.stdin.read().splitlines()
a = data_input[1].split()

tree = BST(a[0])
for el in a[1:]:
    tree.insert(el)


count = 0

def check_ends(node):
    if not node:
        return
    if node.left is None and node.right is None:
        count += 1
        return
    
    check_ends(node.right)
    check_ends(node.left)

check_ends(tree)
