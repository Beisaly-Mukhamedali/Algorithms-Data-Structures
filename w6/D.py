import sys
def parse_date(date):
    day, month, year = map(int, date.split('-'))
    return (year, month, day)

def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence[length // 2]
        pivot_key = parse_date(pivot)
        items_equal = []
        items_lower = []
        items_greater = []
        for item in sequence:
            item_key = parse_date(item)
            if item_key > pivot_key:
                items_greater.append(item)
            elif item_key < pivot_key:
                items_lower.append(item)
            else:
                items_equal.append(item)

        return quick_sort(items_lower) + items_equal + quick_sort(items_greater)

def main():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    date_arr = input_data[1:n + 1]
    sorted_dates = quick_sort(date_arr)

    sys.stdout.write("\n".join(sorted_dates) + "\n")
main()
            