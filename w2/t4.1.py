class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

numbers = list(map(int, input().split()))

head = Node(numbers[0])
curr = head
for number in numbers[1:]:
    curr.next = Node(number)
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
while curr:
    print(curr.val)
    curr = curr.next
