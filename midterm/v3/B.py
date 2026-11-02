import sys
class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

    def insert(self, val):
        curr = self
        while True:
            if val < curr.value:
                if curr.left is None:
                    curr.left = TreeNode(val)
                    break
                curr = curr.left
            elif val > curr.value:
                if curr.right is None:
                    curr.right = TreeNode(val)
                    break
                curr = curr.right

def get_height(node):
    if node is None:
        return 0
    return 1 + max(get_height(node.left), get_height(node.right))

def main():
    inp_data = sys.stdin.read().splitlines()
    arr = list(map(int, inp_data[1].split()))
    node = TreeNode(arr[0])
    for i in arr[1:]:
        node.insert(i)
    print(get_height(node))

main()