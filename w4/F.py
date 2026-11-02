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
    
    def count_triangle(self):
        root = self
        stack = [root]
        triangle_count = 0
        while stack:
            node = stack.pop()
            if node.right and node.left:
                triangle_count += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return triangle_count

lines = sys.stdin.read().splitlines()

a = list(map(int, lines[1].split()))

root = TreeNode(a[0])

for el in a[1:]:
    root.insert(el)

sys.stdout.write(str(root.count_triangle()))