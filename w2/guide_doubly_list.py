class DoublyNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    

head = tail = DoublyNode(1)


def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' <-> '.join(elements))

display(head)

# Insert at beginning - O(1)

def insert_at_beginning(head, tail, val):
    new_node = DoublyNode(val)
    new_node.next = head
    head.prev = new_node
    return new_node, tail

head, tail = insert_at_beginning(head, tail, 3)

display(head)

# Insert at end - O(1)
def insert_at_end(head, tail, val):
    new_node = DoublyNode(val)
    tail.next = new_node
    return head, new_node

head, tail = insert_at_end(head, tail, 7)
display(head)