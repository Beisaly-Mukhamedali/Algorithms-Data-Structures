n = int(input())

arr = []

for _ in range(n):
    name = input()
    arr.append(name)

result = []
for name in arr:
    if not result or result[-1] != name:
        result.append(name)

print(*result)

