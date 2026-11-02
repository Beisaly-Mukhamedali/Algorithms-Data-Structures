class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

input()
numbers = list(map(int, input().split()))
head = Node(numbers[0])
curr = head

for num in numbers[1:]:
    curr.next = Node(num)
    curr = curr.next

curr = head.next
curr_max = head.val
all_max = head.val

while curr:
    curr_max = max(curr.val, curr_max + curr.val)
    all_max = max(curr_max, all_max)
    curr = curr.next

print(all_max)