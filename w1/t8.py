class Stack:
    def __init__(self, size):
        self.max_size = size
        self.top = -1
        self.arr = [None] * size

    def push(self, number):
        if self.top < self.max_size - 1:
            self.top += 1
            self.arr[self.top] = number
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
            return self.arr[self.top]
        else:
            return "!"

    def is_empty(self):
        return self.top == -1

n = int(input())
numbers = list(map(int, input().split()))
stack1 = Stack(n)
result = []

for age in numbers:
    while not stack1.is_empty() and stack1.look_up() >= age:
        stack1.pop()
    if stack1.is_empty():
        result.append(-1)
    else:
        result.append(stack1.look_up())
    stack1.push(age)
                
print(*result)
