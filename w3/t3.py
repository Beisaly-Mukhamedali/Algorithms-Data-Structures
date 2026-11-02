def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return left


_, m = map(int, input().split())

a = list(map(int, input().split()))

p = []
current_sum = 0
for length in a:
    current_sum += length
    p.append(current_sum)

for _ in range(m):
    b = int(input())
    block_idx = binary_search(p, b)
    print(block_idx + 1)
    