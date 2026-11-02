import bisect
import sys

sys.setrecursionlimit(150000)


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
    k = int(data[1])

    if k > n:
        sys.stdout.write("-1\n")
        return

    a = list(map(int, data[2 : n + 2]))

    # 1. Быстрое построение BST за O(N log N)
    root = TreeNode(a[0])
    nodes = {a[0]: root}
    depths = {a[0]: 1}
    sorted_vals = [a[0]]

    for val in a[1:]:
        idx = bisect.bisect_left(sorted_vals, val)

        cand_left = sorted_vals[idx - 1] if idx > 0 else None
        cand_right = sorted_vals[idx] if idx < len(sorted_vals) else None

        depth_l = depths[cand_left] if cand_left is not None else -1
        depth_r = depths[cand_right] if cand_right is not None else -1

        if depth_l > depth_r:
            parent = nodes[cand_left]
            parent.right = TreeNode(val)
            curr = parent.right
        else:
            parent = nodes[cand_right]
            parent.left = TreeNode(val)
            curr = parent.left

        nodes[val] = curr
        depths[val] = depths[parent.value] + 1
        bisect.insort(sorted_vals, val)

    # 2. In-order обход (слева-направо) для поиска K-го элемента
    visited_count = [0]
    ans = [-1]

    def in_order(node):
        if not node or ans[0] != -1:
            return

        in_order(node.left)

        visited_count[0] += 1
        if visited_count[0] == k:
            ans[0] = node.value
            return

        in_order(node.right)

    in_order(root)

    sys.stdout.write(str(ans[0]) + "\n")


if __name__ == "__main__":
    solve()