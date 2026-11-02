class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def _get_node(self, index):
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr

    def insert(self, x, p):
        new_node = Node(x)
        if self.size == 0:
            self.head = self.tail = new_node
        elif p <= 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif p >= self.size:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            curr = self._get_node(p)
            new_node.prev = curr.prev
            new_node.next = curr
            curr.prev.next = new_node
            curr.prev = new_node
        self.size += 1

    def remove(self, p):
        if self.size == 0 or p < 0 or p >= self.size:
            return None
        
        curr = self._get_node(p)
        
        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next

        if curr.next:
            curr.next.prev = curr.prev
        else:
            self.tail = curr.prev

        self.size -= 1
        return curr.val

    def print_list(self):
        if self.size == 0:
            print(-1)
            return
        
        res = []
        curr = self.head
        while curr:
            res.append(str(curr.val))
            curr = curr.next
        print(" ".join(res))

    def replace(self, p1, p2):
        if p1 < 0 or p1 >= self.size:
            return
        val = self.remove(p1)
        self.insert(val, p2)

    def reverse(self):
        if self.size <= 1:
            return
        curr = self.head
        self.tail = self.head
        while curr:
            curr.prev, curr.next = curr.next, curr.prev
            if not curr.prev:
                self.head = curr
            curr = curr.prev

    def cyclic_left(self, x):
        if self.size <= 1:
            return
        x %= self.size
        if x == 0:
            return
        
        new_tail = self._get_node(x - 1)
        new_head = new_tail.next

        new_tail.next = None
        new_head.prev = None
        
        self.tail.next = self.head
        self.head.prev = self.tail
        
        self.head = new_head
        self.tail = new_tail

    def cyclic_right(self, x):
        if self.size <= 1:
            return
        x %= self.size
        if x == 0:
            return
        self.cyclic_left(self.size - x)

dll = DoublyLinkedList()

while True:
    try:
        line = input().strip()
        if not line:
            continue
        
        parts = list(map(int, line.split()))
        cmd = parts[0]

        if cmd == 1:
            dll.insert(parts[1], parts[2])
        elif cmd == 2:
            dll.remove(parts[1])
        elif cmd == 3:
            dll.print_list()
        elif cmd == 4:
            dll.replace(parts[1], parts[2])
        elif cmd == 5:
            dll.reverse()
        elif cmd == 6:
            dll.cyclic_left(parts[1])
        elif cmd == 7:
            dll.cyclic_right(parts[1])
        elif cmd == 0:
            break
    except EOFError:
        break