input()
arr1 = list(map(int, input().split()))
input()
arr2 = list(map(int, input().split()))

print(*sorted(arr1 + arr2))