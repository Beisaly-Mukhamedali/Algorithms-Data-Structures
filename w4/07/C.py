import sys
class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    def insert(self, value):
        curr = self
        while True:
            if value < curr.value:
                if curr.left is None:
                    curr.left = TreeNode(value)
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = TreeNode(value)
                    break
                curr = curr.right

    def find(self, value):
        curr = self
        while curr:
            if value == curr.value:
                return curr
            if value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return None
    
    def subtree(self, value):
        curr = find(value)
        stack = [curr]
        result = []

        while stack:
            node = stack.pop()
            result.append(str(node.value))

            if node.right:
                result.append(node.right)
            if node.left:
                result.append(node.left)
        return result