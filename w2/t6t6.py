class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def headMaker(input_line):
    arr = list(map(int, input_line.split()))
    length = arr[0]
    if length < 1:
        return
    head = Node(arr[1])
    curr = head
    for num in arr[2:]:
        curr.next = Node(num)
        curr = curr.next
    return head

head1 = headMaker(input())
head2 = headMaker(input())

l1, l2 = head1, head2
mergedl = Node(0)
curr = mergedl
while l1 and l2:
    if l1.val <= l2.val:
        curr.next = l1
        l1 = l1.next
    else:
        curr.next = l2
        l2 = l2.next
    curr = curr.next
if l1:
    curr.next = l1
elif l2:
    curr.next = l2
result = []
mergedl = mergedl.next
curr = mergedl
while curr:
    result.append(curr.val)
    curr = curr.next

print(*result)