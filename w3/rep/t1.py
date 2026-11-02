import sys
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

input_lines = sys.stdin.read().splitlines()
arr = input_lines[1]
target = input_lines[2]


print(binary_search(arr, target))