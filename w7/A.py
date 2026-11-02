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

    l = r = 0
    
    L_len = len(L)
    R_len = len(R)
    sorted_arr = [0] * n
    i = 0

    while l < L_len and r < R_len:
        if len(L[l]) <= len(R[r]):
            sorted_arr[i] = L[l]
            l += 1
        else:
            sorted_arr[i] = R[r]
            r += 1
        i += 1
    
    while l < L_len:
        sorted_arr[i] = L[l]
        i += 1
        l += 1
    while r < R_len:
        sorted_arr[i] = R[r]
        i += 1
        r += 1

    return sorted_arr


def main():
    input_data = sys.stdin.read().splitlines()
    T = int(input_data[0])
    result = []
    for k in range(T):
        strings = input_data[k + 1].split()
        sorted_string = merge_sort(strings)
        result.append(" ".join(sorted_string))
    
    print("\n".join(result))



main()