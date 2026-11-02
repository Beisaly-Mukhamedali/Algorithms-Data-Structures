import sys
import heapq

def main():
    input_data = sys.stdin.read().splitlines()
    n = input_data[0]
    a = list(map(int, input_data[1].split()))
    heapq.heapify(a)
    total_cost = 0

    while len(a) > 1:
        first = heapq.heappop(a)
        second = heapq.heappop(a)
        cost = first + second
        total_cost += cost
        heapq.heappush(a, cost)

    print(total_cost)

main()