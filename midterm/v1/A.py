import sys
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

input_data = sys.stdin.read().splitlines()
arr = list(map(int, input_data[1].split()))
x = int(input_data[2])

head = Node(arr[0])
curr = head
for i in arr[1:]:
    curr.next = Node(i)
    curr = curr.next
dummy = Node(0)
dummy.next = head
curr = dummy

res = []
while curr.next:
    if curr.next.value == x:
        curr.next = curr.next.next
    else:
        curr = curr.next
curr = head
while curr:
    res.append(curr.value)
    curr = curr.next

print(*res)