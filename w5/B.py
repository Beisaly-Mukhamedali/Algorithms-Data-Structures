import sys
import heapq

def main():
    input_data = sys.stdin.read().splitlines()
    stones = [-int(x) for x in input_data[1].split()]
    heapq.heapify(stones)
    while len(stones) > 1:
        y = -heapq.heappop(stones)
        x = -heapq.heappop(stones)

        if y != x:
            heapq.heappush(stones, -(y - x))
    if stones:
        print(-stones[0])
    else:
        print(0)

main()
