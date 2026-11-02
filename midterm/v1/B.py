import sys
from bisect import bisect_right

def main():
    input_data = sys.stdin.read().splitlines()
    arr = list(map(int, input_data[1].split()))
    out = []
    R = range(10**9 + 1)
    for m in arr:
        ans = bisect_right(R, m, key= lambda r: r*r) - 1
        out.append(str(ans))
    print("\n".join(out))
main()