import sys
sys.setrecursionlimit(300000)
def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence[length // 2]
    
    items_greater = []
    items_lower = []
    items_equal = []
    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        elif item == pivot:
            items_equal.append(item)
        else:
            items_lower.append(item)
    
    return quick_sort(items_lower) + items_equal + quick_sort(items_greater)

def main():
    input_data = sys.stdin.read().splitlines()
    letters = input_data[1]
    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    vowels = []
    consonants = []
    for char in letters:
        if char in vowel_set:
            vowels.append(char)
        else:
            consonants.append(char)
    srted = quick_sort(vowels) + quick_sort(consonants)
    sys.stdout.write("".join(srted) + "\n")
main()