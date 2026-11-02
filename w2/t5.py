class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

n = int(input())
numbers = list(map(int, input().split()))

head = Node(numbers[0])
curr = head

for number in numbers[1:]:
    curr.next = Node(number)
    curr = curr.next

mid = n // 2
count = 0

if mid == 0:
    head = head.next
else:
    curr = head
    while curr:
        if count == (mid - 1):
            curr.next = curr.next.next
        curr = curr.next
        count += 1

curr = head
result = []

while curr:
    result.append(curr.val)
    curr = curr.next

print(*result)