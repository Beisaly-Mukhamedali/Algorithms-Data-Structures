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
    def inorder_travesal(self):
        curr = self
        stack = []
        result = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append()
            curr = curr.right
        return result


