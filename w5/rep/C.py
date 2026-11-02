import sys
import heapq

def main():
    input_data = sys.stdin.read().splitlines()
    n, x = map(int, input_data[0].split())
    a = [-int(val) for val in input_data[1].split()]
    heapq.heapify(a)
    total_money = 0
    for _ in range(x):
        max_seats = -heapq.heappop(a)
        total_money += max_seats
        
        max_seats -= 1

        if max_seats > 0:
            heapq.heappush(a, -max_seats)
    print(total_money)

main()
            
        
    