class Stack:
    def __init__(self, size):
        self.max_size = size
        self.top = -1
        self.arr = []

    def push(self, letter):
        if self.top < self.max_size - 1:
            if letter == "#":
                self.pop()
            else:
                self.top += 1
                self.arr.append(letter)
        else:
            print("!")

    def pop(self):
        if self.top > -1:
            val = self.arr[self.top]
            self.top -= 1
            return val
        else:
            print("!")
            return None
    
    def look_up(self):
        if self.top > -1:
            return self.arr[top]
        else:
            return "!"

    def is_empty(self):
        return self.top == -1


stack1 = Stack(100000)