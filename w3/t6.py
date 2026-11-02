import math

def check(bags, k, h):
    total_hours = 0
    for bag in bags:
        total_hours += math.ceil(bag / k)
    return total_hours <= h

n, h = map(int, input().split())

bags = list(map(int, input().split()))

left = 1
right = max(bags)

while left < right:
    mid = (left + right) // 2
    if check(bags, mid, h):
        right = mid
    else:
        left = mid + 1

print(left)