class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

input()
values = list(map(int, input().split())) 

head = Node(values[0])
curr = head

for val in values[1:]:
    curr.next = Node(val)
    curr = curr.next

curr = head
prev = None

while curr is not None:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt

head = prev
curr = prev
result = []

while curr is not None:
    result.append(curr.val)
    curr = curr.next

print(*result)