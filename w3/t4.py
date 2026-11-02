def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    count = 0

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            count = mid + 1
            left = mid + 1
        else:
            right = mid - 1
    return count

n = int(input())

a = list(map(int, input().split()))

p_rounds = int(input())

a.sort()

prefix_sums = [0] * (n + 1)
for i in range(n):
    prefix_sums[i + 1] = prefix_sums[i] + a[i]

for _ in range(p_rounds):
    p_i = int(input())

    count = binary_search(a, p_i)

    total_power = prefix_sums[count]

    print(count, total_power)