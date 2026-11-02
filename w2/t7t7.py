class Node:
    def __init__(self, val):
        self.val = val
        self.next = next
n, k = map(int, input().split())
stream = input().split()

head = Node(stream[0])
curr = head

for word in stream[1:]:
    curr.next = Node(word)
    curr = curr.next
tail = curr
new_tail = head

for _ in range(k - 1):
    new_tail = new_tail.next
new_head = new_tail.next

tail.next = head

new_tail.next = None

curr = new_head

while curr:
    print(curr.val)