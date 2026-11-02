import sys
sys.setrecursionlimit(300000)
def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence[length // 2]
    
    items_greater = []
    items_lower = []
    items_equal = []
    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        elif item == pivot:
            items_equal.append(item)
        else:
            items_lower.append(item)
    
    return quick_sort(items_lower) + items_equal + quick_sort(items_greater)


def main():
    input_data = sys.stdin.read().split()
    n, m = int(input_data[0]), int(input_data[1])
    idx = 2
    a, b = [int(x) for x in input_data[idx : idx + n]], [int(x) for x in input_data[idx + n : idx + n + m]]
    if not a or not b:
        print()
        return
    sorted_a, sorted_b = quick_sort(a), quick_sort(b)
    result = []
    i, j = 0, 0
    while i < len(sorted_a) and j < len(sorted_b):
        if sorted_a[i] == sorted_b[j]:
            result.append(sorted_a[i])
            i += 1
            j += 1
        elif sorted_a[i] < sorted_b[j]:
            i += 1
        else:
            j += 1
    print(*result)

main()