class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def headMaker(inp_list):
    listed_inp = list(map(int, inp_list.split()))
    length = listed_inp[0]
    if length < 1:
        return
    head = Node(listed_inp[1])
    curr = head
    for num in listed_inp[2:]:
        curr.next = Node(num)
        curr = curr.next
    return head

head1 = headMaker()
