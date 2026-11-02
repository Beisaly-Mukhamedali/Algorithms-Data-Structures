import sys

# Qatylardy tereńdetý úshın rekýrsııa lı mıtın úlkeytemiz
sys.setrecursionlimit(300000)

GRADE_MAP = {
    'A+': 4.00,
    'A': 3.75,
    'B+': 3.50,
    'B': 3.00,
    'C+': 2.50,
    'C': 2.00,
    'D+': 1.50,
    'D': 1.00,
    'F': 0.00,
}


def quick_sort(sequence):
  length = len(sequence)
  if length <= 1:
    return sequence
  else:
    pivot = sequence[length // 2]

  items_greater = []
  items_lower = []
  items_equal = []

  # Kortezderdi salystyratyndyqtan, (GPA, Lastname, Firstname) avtomatty túrde durys surttalady
  for item in sequence:
    if item > pivot:
      items_greater.append(item)
    elif item == pivot:
      items_equal.append(item)
    else:
      items_lower.append(item)

  return quick_sort(items_lower) + items_equal + quick_sort(items_greater)


def main():
  lines = sys.stdin.read().splitlines()
  if not lines:
    return

  n = int(lines[0].strip())
  students = []

  for i in range(1, n + 1):
    parts = lines[i].split()

    lastname = parts[0]
    firstname = parts[1]
    m = int(parts[2])

    total_points = 0.0
    total_credits = 0

    idx = 3
    for _ in range(m):
      grade = parts[idx]
      credits = int(parts[idx + 1])

      total_points += GRADE_MAP[grade] * credits
      total_credits += credits

      idx += 2

    gpa = total_points / total_credits
    # Сatarda (gpa, lastname, firstname) saqtaımyz
    students.append((gpa, lastname, firstname))

  # Vstroitelnyı sort ornyna self-made quick_sort paidalanamyz
  sorted_students = quick_sort(students)

  for gpa, lastname, firstname in sorted_students:
    print(f'{lastname} {firstname} {gpa:.3f}')


if __name__ == '__main__':
  main()