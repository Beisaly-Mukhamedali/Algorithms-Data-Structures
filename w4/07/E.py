import sys
from collections import deque
class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

lines = sys.stdin.read().splitlines()

n = int(lines[0])

nodes = [None] + [int(x) for x in range(1,n + 1)]

for line in lines[1:]:
    x, y, z = map(int, line.split())
    node = TreeNode(x)
    if z == 0:
        nodes[x].left = nodes[y]
    else:
        nodes[x].right = node[y]

root = nodes[1]
queue = deque([root])
max_width = 0
while queue:
    current_width = len(queue)
    max_width = max(max_width, current_width)

    for _ in range(current_width):
        curr_node = queue.popleft()
        if curr_node.left:
            curr_node = curr_node.left
        if curr_node.right:
            curr_node = curr.right

print(max_width)
        

    