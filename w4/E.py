from collections import deque
import sys

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

lines = sys.stdin.read().splitlines()

n = int(lines[0])

nodes = [None] + [TreeNode(i) for i in range(1, n + 1)]

for line in lines[1:]:
    line_str = line.strip()
    if not line_str:
        continue
    x, y, z = map(int, line_str.split())
    if z == 0:
        nodes[x].left = nodes[y]
    else:
        nodes[x].right = nodes[y]

root = nodes[1]
queue = deque([root])
max_width = 0

while queue:
    current_width = len(queue)
    max_width = max(max_width, current_width)

    for _ in range(current_width):
        curr_node = queue.popleft()
        if curr_node.left:
            queue.append(curr_node.left)
        if curr_node.right:
            queue.append(curr_node.right)
    
print(max_width)
