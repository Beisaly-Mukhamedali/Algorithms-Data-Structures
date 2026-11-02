import sys

class DoublyNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_front(self, val):
        new_node = DoublyNode(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        return "ok"

    def add_back(self, val):
        new_node = DoublyNode(val)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        return 'ok'
    
    def erase_front(self):
        if not self.head:
            return 'error'
        val = self.head.val
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return val

    def erase_back(self):
        if not self.tail:
            return 'error'
        val = self.tail.val
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return val
    
    def front(self):
        if not self.head:
            return 'error'
        else:
            return self.head.val
    
    def back(self):
        if not self.tail:
            return 'error'
        else:
            return self.tail.val

    def clear(self):
        self.head = None
        self.tail = None
        return "ok"

lines = sys.stdin.read().splitlines()
dll = DoublyLinkedList()
out = []
for line in lines:
    if not line:
        continue
    parts = line.split()
    cmd = parts[0]
    if cmd == "add_front":
        out.append(dll.add_front(parts[1]))
    elif cmd == "add_back":
        out.append(dll.add_back(parts[1]))
    elif cmd == "erase_front":
        out.append(dll.erase_front())
    elif cmd == "erase_back":
        out.append(dll.erase_back())
    elif cmd == "front":
        out.append(dll.front())
    elif cmd == "back":
        out.append(dll.back())
    elif cmd == "clear":
        out.append(dll.clear())
    elif cmd == "exit":
        out.append("goodbye")
        break

print("\n".join(out))
    