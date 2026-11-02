def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

input()
arr = list(map(int, input().split()))
target = int(input())

print(binary_search(arr, target))