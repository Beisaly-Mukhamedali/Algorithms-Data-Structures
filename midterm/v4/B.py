class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
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

def preorder_travesal(root):
    if not root:
        return []
    return [root.value] + preorder_travesal(root.left) + preorder_travesal(root.right)
def main():
    input()
    arr = list(map(int, input().split()))
    node = TreeNode(arr[0])
    for i in arr[1:]:
        node.insert(i)
    print(*preorder_travesal(node))

main()