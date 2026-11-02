from collections import deque
import sys

def main():
    input_data = sys.stdin.read().splitlines()
    queue = deque()
    result = []
    for input_line in input_data[1:]:
        line = list(input_line.split())
        cmd = line[0]
        if cmd == "push":
            num = line[1]
            queue.append(num)
        else:
            result.append(queue.popleft())
    
    sys.stdout.write("\n".join(result) + "\n")

main()
            