import sys
import heapq

def main():
    input_data = sys.stdin.read().splitlines()

    q, k = map(int, input_data().split())
    
    min_heap = []
    current_sum = 0
    output = []

    for line in input_data[1:q + 1]:
        cmd = line.split()
        if cmd[0] == "insert":
            num = int(cmd[1])
            heapq.heappush(min_heap, num)
            current_sum += num

            if len(min_heap) > k:
                removed = heapq.heappop(min_heap)
                current_sum -= removed
        elif cmd[0] == "print":
            output.append(str(current_sum))

    sys.stdout.write("\n".join(output) + "\n")

main()