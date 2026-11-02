import sys
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
    
    return quick_sort(items_greater) + items_equal + quick_sort(items_lower)
    
def main():
    data_input = sys.stdin.read().splitlines()
    n, m = map(int, data_input[0].split())
    matrix = []
    for arr in data_input[1:]:
        matrix.append(list(map(int, arr.split())))
    result = [[0] * m for _ in range(n)]

    for j in range(m):
        col = [matrix[i][j] for i in range(n)]
        sorted_col = quick_sort(col)
        
        for i in range(n):
            result[i][j] = sorted_col[i]
    
    for row in result:
        print(*row)



main()

