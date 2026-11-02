import sys
import heapq

def main():
    input_data = sys.stdin.read().splitlines()
    q, k = map(int, input_data[0].split())
    min_heap = []
    output = []
    total = 0
    for line in input_data[1:q+1]:
        
    sys.stdout.write("\n".join(output) + "\n")

main()

