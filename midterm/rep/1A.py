input()
arr = list(map(int, input().split()))
x = int(input())
result = [int(i) for i in arr if i != x]
print(*result)