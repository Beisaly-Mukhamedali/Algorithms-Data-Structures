import sys

def main():
    inp_data = sys.stdin.read().splitlines()
    arr = []
    for line in inp_data[1:]:
        line = line.split()
        name, grade = line[0], int(line[1])
        arr.append((name, grade))
    arr.sort(key=lambda x: x[1])
    for name, grade in arr:
        print(name)
main()