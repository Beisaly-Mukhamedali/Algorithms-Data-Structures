class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
    def inorder_travesal(self):
        if self.left:
            self.left.inorder_travesal()
        print(self.value)
        if self.right:
            self.right.inorder_travesal()
    def preorder_travesal(self):
        print(self.value)
        if self.left:
            self.left.preorder_travesal()
        if self.right:
            self.right.preorder_travesal()
    def postorder_travesal(self):
        if self.left:
            self.left.postorder_travesal()
        if self.right:
            self.right.postorder_travesal()
        print(self.value)
    
    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True

