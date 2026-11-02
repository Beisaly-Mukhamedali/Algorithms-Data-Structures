class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

input()
stream = input().split()

head = Node(stream[0])
curr = head

for num in stream[1:]:
    curr.next = Node(num)
    curr = curr.next

curr = head
prev = None
while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt

head = prev
curr = head
result = []
while curr:
    result.append(curr.val)
    curr = curr.next

print(*result)
