import sys
def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    m = n // 2
    L = arr[:m]
    R = arr[m:]

    L = merge_sort(L)
    R = merge_sort(R)
    len_L = len(L)
    len_R = len(R)
    l = r = 0
    i = 0
    sorted_arr = [0] * n
    while l < len_L and r < len_R:
        if L[l] <= R[r]:
            sorted_arr[i] = L[l]
            l += 1
        else:
            sorted_arr[i] = R[r]
            r += 1
        i += 1
    
    while l < len_L:
        sorted_arr[i] = L[l]
        l += 1
        i += 1
    while r < len_R:
        sorted_arr[i] = R[r]
        r += 1
        i += 1
    return sorted_arr

def main():
    input_data = sys.stdin.read().splitlines()
    arr1 = list(map(int, input_data[1].split()))
    arr2 = list(map(int, input_data[3].split()))
    total_arr = arr1 + arr2
    print(*merge_sort(total_arr))
main()
