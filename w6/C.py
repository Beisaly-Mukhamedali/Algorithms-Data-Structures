import sys

def main():
    input_data = sys.stdin.read().splitlines()
    arr = list(map(int, input_data[1].split()))
    arr_sorted = sorted(arr)
    min_diff = float("inf")
    result = []
    for i in range(len(arr_sorted) - 1):
        diff = arr_sorted[i + 1] - arr_sorted[i]
        if diff < min_diff:
            min_diff = diff
    
    for i in range(len(arr_sorted) - 1):
        a, b = arr_sorted[i], arr_sorted[i + 1]
        if b - a == min_diff:
            result.append(a)
            result.append(b)
    
    print(*result)
main()