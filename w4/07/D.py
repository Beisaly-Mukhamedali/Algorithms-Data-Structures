import sys
from collections import deque
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


def get_level_sums(root):
    if not root:
        return 0, []
    queue = deque([root])
    level_sums = []
    while queue:
        level_size = len(queue)
        current_sum = 0
        for _ in range(level_size):
            node = queue.popleft()
            current_sum += node.value

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level_sums.append(str(current_sum))