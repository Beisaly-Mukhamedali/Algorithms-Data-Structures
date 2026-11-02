n = int(input())
names = []
for _ in range(n):
    name = input()
    names.append(name)
result = []
for name in names:
    if not result or result[-1] != name:
        result.append(name)

print(len(result))
for i in result:
    print(i)
