import sys

# Настройка лимита рекурсии
sys.setrecursionlimit(300000)


def quick_sort(sequence):
  length = len(sequence)
  if length <= 1:
    return sequence

  pivot = sequence[length // 2]

  items_lower = []
  items_equal = []
  items_greater = []

  # Кортежи (original, current) автоматически сравниваются по first элементу (original)
  for item in sequence:
    if item < pivot:
      items_lower.append(item)
    elif item == pivot:
      items_equal.append(item)
    else:
      items_greater.append(item)

  return quick_sort(items_lower) + items_equal + quick_sort(items_greater)


def main():
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  n = int(input_data[0])

  # current_to_original[new_nick] = original_nick
  current_to_original = {}

  idx = 1
  for _ in range(n):
    old_nick = input_data[idx]
    new_nick = input_data[idx + 1]
    idx += 2

    if old_nick in current_to_original:
      # Игрок меняет ник уже не в первый раз
      original = current_to_original[old_nick]
      del current_to_original[old_nick]
      current_to_original[new_nick] = original
    else:
      # Первая смена ника для этого игрока
      current_to_original[new_nick] = old_nick

  # Собираем список пар (original_nick, current_nick)
  result_pairs = [
      (original, current) for current, original in current_to_original.items()
  ]

  # Сортируем с помощью QuickSort по изначальному нику
  sorted_pairs = quick_sort(result_pairs)

  # Вывод
  print(len(sorted_pairs))
  for original, current in sorted_pairs:
    print(f'{original} {current}')


if __name__ == '__main__':
  main()