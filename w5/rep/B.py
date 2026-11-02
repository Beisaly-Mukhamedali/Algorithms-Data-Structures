import sys
import heapq

def main():
    input_data = sys.stdin.read().splitlines()
    a = [-int(x) for x in input_data[1].split()]
    heapq.heapify(a)
    while len(a) > 1:
        y, x = -heapq.heappop(a), -heapq.heappop(a)
        if y != x:
            heapq.heappush(a, -(y - x))
    if a:
        print(-a[0])
    else:
        print(0)

main()
        