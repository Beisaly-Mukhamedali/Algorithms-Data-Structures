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
        if sum(L[l]) < sum(R[r]):
            sorted_arr[i] = R[r]
            r += 1
        elif sum(L[l]) == sum(R[r]):
            if L[l] <= R[r]:
                sorted_arr[i] = L[l]
                l += 1
            else:
                sorted_arr[i] = R[r]
                r += 1
        elif sum(L[l]) > sum(R[r]):
            sorted_arr[i] = L[l]
            l += 1
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
    n, m = map(int, input_data[0].split())
    inp = input_data[1:]
    array = []

    for i in range(1, n + 1):
        row = list(map(int, input_data[i].split()))
        array.append(row)
    result = merge_sort(array)
    for row in result:
        print(*row)
    
main()