def nugman(arr):
    stack = []
    result = []
    for age in arr:
        while not len(stack) == 0 and stack[-1] >= age:
            stack.pop()
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack[-1])
        stack.append(age)
    return result


input()
arr = list(map(int, input().split()))

print(*nugman(arr))
