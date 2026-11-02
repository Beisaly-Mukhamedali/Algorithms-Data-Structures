import sys
from bisect import bisect_left

def binary_search_exact(arr, target):
    idx = bisect_left(arr, target)

    if idx < len(arr) and arr[idx] == target:
        return idx
    else:
        return -1

def main():
    inp = sys.stdin.read().splitlines()
    arr = list(map(int, inp[1].split()))
    queries = list(map(int, inp[3].split()))
    result = []
    for q in queries:
        if binary_search_exact(arr, q) == -1:
            result.append("NO")
        else:
            result.append("YES")
    sys.stdout.write("\n".join(result) + "\n")
main()