import sys
from bisect import bisect_left, bisect_right

def main():
    inp = sys.stdin.read().splitlines()
    arr = list(map(int, inp[1].split()))
    queries = list(map(int, inp[3].split()))
    result = []
    for q in queries:
        number = bisect_right(arr, q) - bisect_left(arr, q)
        result.append(str(number))
    sys.stdout.write("\n".join(result) + "\n")
main()