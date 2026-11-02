import bisect
import sys

# Поднимаем лимит рекурсии для обхода глубоких деревьев
sys.setrecursionlimit(30000)


class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    if n == 0:
        sys.stdout.write("0\n")
        return

    raw_a = list(map(int, data[1 : n + 1]))

    # Сохраняем элементы без повторов (дубликаты не вставляются)
    a = []
    seen = set()
    for x in raw_a:
        if x not in seen:
            seen.add(x)
            a.append(x)

    if not a:
        sys.stdout.write("0\n")
        return

    # --- Построение BST за O(N log N) ---
    root = TreeNode(a[0])
    nodes = {a[0]: root}
    depths = {a[0]: 1}
    sorted_vals = [a[0]]

    for val in a[1:]:
        idx = bisect.bisect_left(sorted_vals, val)

        left_val = sorted_vals[idx - 1] if idx > 0 else None
        right_val = sorted_vals[idx] if idx < len(sorted_vals) else None

        depth_l = depths[left_val] if left_val is not None else -1
        depth_r = depths[right_val] if right_val is not None else -1

        # Выбираем родителя с большей глубиной
        if depth_l > depth_r:
            parent = nodes[left_val]
            parent.right = TreeNode(val)
            curr = parent.right
        else:
            parent = nodes[right_val]
            parent.left = TreeNode(val)
            curr = parent.left

        nodes[val] = curr
        depths[val] = depths[parent.value] + 1
        bisect.insort(sorted_vals, val)

    # --- Подсчёт максимального расстояния (диаметра) ---
    max_diameter = [0]

    def get_height(node):
        if not node:
            return 0

        left_h = get_height(node.left)
        right_h = get_height(node.right)

        current_path = left_h + right_h + 1
        if current_path > max_diameter[0]:
            max_diameter[0] = current_path

        return max(left_h, right_h) + 1

    get_height(root)
    sys.stdout.write(str(max_diameter[0]) + "\n")


if __name__ == "__main__":
    solve()