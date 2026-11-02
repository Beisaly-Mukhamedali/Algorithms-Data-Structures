def binary_search(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1
    return -1

def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return -1

def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left= mid + 1


numbers = [1, 2, 2, 2, 2, 3, 4, 5, 6]


# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         if arr[mid] > target:
#             right = mid
#         else:
#             left = mid + 1
#     return -1

# numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]  # Массив ДОЛЖЕН быть отсортирован
# target = 23

# result = binary_search(numbers, target)

# if result != -1:
#     print(f"Элемент найден на индексе: {result}")
# else:
#     print("Элемент не найден")