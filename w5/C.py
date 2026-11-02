import sys
import heapq

def main():
    input_data = sys.stdin.read().splitlines()
    n, x = map(int, input_data[0].split())
    seats = [-int(val) for val in input_data[1].split()]
    heapq.heapify(seats)
    total_money = 0
    for _ in range(x):
        max_seats = -heapq.heappop(seats)
        total_money += max_seats
        max_seats -= 1
        if max_seats > 0:
            heapq.heappush(seats, -max_seats)

    print(total_money)

main()  