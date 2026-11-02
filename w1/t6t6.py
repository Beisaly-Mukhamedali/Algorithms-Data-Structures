def edit(string):
    stack = []
    for char in string:
        if char == "#":
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)

a, b = input().split()
print(edit(a) == edit(b))