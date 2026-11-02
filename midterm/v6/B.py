import sys
from bisect import bisect_left

def main():
    input_data = sys.stdin.read().splitlines()
    arr = list(map(int, input_data[1].split()))
    queries = list(map(int, input_data[3].split()))
    result = []
    for q in queries:
        idx = bisect_left(arr, q)
        if idx == len(arr):
            result.append(str(-1))
        else:
            result.append(str(idx + 1))
    sys.stdout.write("\n".join(result) + "\n")

main()