class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

n = int(input())
values = list(map(int, input().split()))

head = Node(values[0])

curr = head

for val in values[1:]:
    curr.next = Node(val)
    curr = curr.next

curr = head

while curr is not None and curr.next is not None:
    curr.next = curr.next.next
    curr = curr.next

result = []
curr = head

while curr is not None:
    result.append(curr.val)
    curr = curr.next

print(*result)