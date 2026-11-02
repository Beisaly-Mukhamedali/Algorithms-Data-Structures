from collections import deque 
class TreeNode:

  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

  def insert(self, value):
    curr = self
    while True:
      # Equal values go to left subtree per problem rule
      if value <= curr.value:  #[cite: 1]
        if curr.left is None:
          curr.left = TreeNode(value)
          break
        curr = curr.left
      else:
        if curr.right is None:
          curr.right = TreeNode(value)
          break
        curr = curr.right

  def inorder_travesal(self):
    stack = []
    curr = self
    while curr or stack:
      while curr:
        stack.append(curr)
        curr = curr.left
      curr = stack.pop()
      print(curr.value)
      curr = curr.right

  def preorder_travesal(self):
    stack = [self]
    while stack:
      curr = stack.pop()
      print(curr.value)
      # Push right first so left gets popped/processed first
      if curr.right:
        stack.append(curr.right)
      if curr.left:
        stack.append(curr.left)

  def postorder_travesal(self):
    stack1 = [self]
    stack2 = []
    while stack1:
      curr = stack1.pop()
      stack2.append(curr)
      if curr.left:
        stack1.append(curr.left)
      if curr.right:
        stack1.append(curr.right)

    while stack2:
      print(stack2.pop().value)

  def find(self, value):
    curr = self
    while curr:
      if value == curr.value:
        return True
      elif value <= curr.value:  # Matches the left subtree rule for <=
        curr = curr.left
      else:
        curr = curr.right
    return False
  

# BFS


def BFS(root):
  if not root:
    return []
  queue = deque([root])
  level_sums = []
  while queue:
    level_size = len(queue)
    current_sum = 0
    for _ in range(level_size):
      node = queue.popleft()
      current_sum += node.value
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
      level_sums.append(str(current_sum))  
  return level_sums

def subtree_count(root, x):
        curr = root.find(x)
        stack = [curr]
        count = 0
        while stack:
            node = stack.pop()
            count += 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return count












class TreeNode:
  def __init__(self, value):
    value = value
    self.left = None
    self.right = None
  
  def insert(self, value):
    curr = self
    while True:
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

  def inorder_travesal(self):
    stack = []
    curr = self
    while stack or curr:
      while curr:
        stack.append(curr)
        curr = curr.left
      curr = stack.pop()
      print(curr.value)
      curr = curr.right
    