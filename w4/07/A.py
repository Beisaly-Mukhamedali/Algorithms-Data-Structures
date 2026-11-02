import sys

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def insert(self, value):
        depth = 0
        curr = self
        while True:
            if depth > 100:
                break
            if value <= curr.value:
                if curr.left is None:
                    curr.left = TreeNode(value)
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = TreeNode(value)
                    break
                curr = curr.right
            depth += 1
    def find(self, move):
        curr = self
        for path in move:
            if path == "L":
                if curr.left is None:
                    return False
                curr = curr.left
            elif path == "R":
                if curr.right is None:
                    return False
                curr = curr.right
        return True

data_input = sys.stdin.read().splitlines()

a = list(map(int, data_input[1].split()))
tree = TreeNode(a[0])

for i in a[1:]:
    tree.insert(i)

moves = data_input[2:]
result = []
for move in moves:
    if tree.find(move):
        result.append("YES")
    else:
        result.append("NO")

sys.stdout.write("\n".join(result) + "\n")

"""
9 4
7 10 12 8 5 6 2 1 4
LLL
RRR
RL
RR
"""