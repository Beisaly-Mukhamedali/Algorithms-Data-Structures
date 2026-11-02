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

current_sum = [0]
for el in a[1:]:
    tree.insert(el)

result = []

def count_collect(node):
    if not node:
        return
    
    collect_sum(node.right)
    current_sum[0] += node.value
    node.value = current_sum[0]
    result.append(str(node.value))
    collect_sum(node.left)

count_collect(tree)
