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

def count_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1 
    return count_leaves(root.left) + count_leaves(root.right)

def main():
    input()
    arr = list(map(int, input().split()))
    node = TreeNode(arr[0])
    for i in arr[1:]:
        node.insert(i)
    print(count_leaves(node))

main()