def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (right + left) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left

def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (right + left) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left

def count_in_range(arr, l, r):
    if l > r:
        return 0
    return upper_bound(arr, r) - lower_bound(arr, l)

n, q = map(int, input().split())

a = list(map(int, input().split()))

a.sort()

results = []

for _ in range(q):
    l1, r1, l2, r2 = map(int, input().split())
    
    if l1 > l2:
        l1, r1, l2, r2 = l2, r2, l1, r1
    
    if l2 <= r1:
        ans = count_in_range(a, l1, max(r1, r2))
    else:
        ans = count_in_range(a, l1, r1) + count_in_range(a, l2, r2)
    results.append(str(ans))

print("\n".join(results))