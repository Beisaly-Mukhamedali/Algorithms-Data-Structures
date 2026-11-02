import sys

# Поднимаем лимит рекурсии на случай глубокого вырожденного дерева (до 5000)
sys.setrecursionlimit(10000)


class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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


def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    if n == 0:
        sys.stdout.write("0\n")
        return

    p = list(map(int, data[1 : n + 1]))

    # 1. Честное построение BST
    root = TreeNode(p[0])
    for val in p[1:]:
        root.insert(val)

    # 2. Подсчёт листьев (узлов без детей)
    leaf_count = [0]

    def count_leaves(node):
        if not node:
            return

        # Если у узла нет ни левого, ни правого ребёнка — это лист
        if node.left is None and node.right is None:
            leaf_count[0] += 1
            return

        count_leaves(node.left)
        count_leaves(node.right)

    count_leaves(root)

    sys.stdout.write(str(leaf_count[0]) + "\n")


if __name__ == "__main__":
    solve()