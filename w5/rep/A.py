import sys
import heapq

def main():
    input_data = sys.stdin.read().splitlines()
    a = list(map(int, input_data[1].split()))
    heapq.heapify(a)
    total_cost = 0
    while len(a) > 1:
        first = heapq.heappop(a)
        second = heapq.heappop(a)
        num = first + second
        total_cost += num
        heapq.heappush(a, num)
        
    print(total_cost)
        
main()