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

    def preorder_travesal(self, value):
        curr = self.find(value)
        stack = [curr]
        result = []
        while stack:
            node = stack.pop()
            result.append(str(node.value))
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result


data_input = sys.stdin.read().splitlines()
a = list(map(int, data_input[1].split()))
tree = TreeNode(a[0])
for el in a[1:]:
    tree.insert(el)
k = int(data_input[2])
result = tree.preorder_travesal(k)
sys.stdout.write(" ".join(tree.preorder_travesal(k)))
