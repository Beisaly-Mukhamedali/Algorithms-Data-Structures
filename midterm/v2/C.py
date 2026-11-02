import sys

input_data = sys.stdin.read().splitlines()

n = int(input_data[0])
inp_lines = input_data[1:]
arr = []
for inp_line in input_data[1:]:
    line = inp_line.split()
    name, score = line[0], int(line[1])
    arr.append((name, score))

arr.sort(key=lambda x: (-x[1], x[0]))
print(arr)
