from bisect import bisect_right
import sys


def main():
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  n = int(input_data[0])  #[cite: 8]
  letters = input_data[1 : n + 1]  #[cite: 8]
  k = input_data[n + 1]  #[cite: 8]

  # bisect_right находит индекс первого элемента, который строго больше k
  idx = bisect_right(letters, k)

  # Если idx == n, значит элементов больше k нет, берем letters[0][cite: 8]
  if idx == n:
    print(letters[0])  #[cite: 8]
  else:
    print(letters[idx])


if __name__ == '__main__':
  main()