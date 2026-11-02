import sys

sys.setrecursionlimit(2000)


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
        return

    elements = list(map(int, data[1 : n + 1]))

    # 1. Честное построение Binary Search Tree
    root = TreeNode(elements[0])
    for val in elements[1:]:
        root.insert(val)

    # 2. Обход Right -> Node -> Left
    # Накапливаем сумму и сразу складываем новые значения узлов в результат.
    # Так как мы идём от БОЛЬШИХ элементов к МЕНЬШИМ,
    # итоговые суммы будут получаться сразу в ПОРЯДКЕ ВОЗРАСТАНИЯ (8, 15, 21 ... 36).
    current_sum = [0]
    result = []

    def convert_and_collect(node):
        if not node:
            return

        # Сначала обрабатываем большее (правое) поддерево
        convert_and_collect(node.right)

        # Обновляем текущий узел
        current_sum[0] += node.value
        node.value = current_sum[0]
        result.append(str(node.value))

        # Затем меньшее (левое) поддерево
        convert_and_collect(node.left)

    convert_and_collect(root)

    sys.stdout.write(" ".join(result) + "\n")


if __name__ == "__main__":
    solve()