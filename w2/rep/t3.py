n = int(input())
stream = []
for _ in range(n):
    stream.append(input())

result = []

for name in stream:
    if not result or result[-1] != name:
        result.append(name)

print(len(result))
for h in result:
    print(h)