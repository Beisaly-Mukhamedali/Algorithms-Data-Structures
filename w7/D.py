import sys

def merge_sort_and_count(arr):
    n = len(arr)
    # Базовый случай: в массиве из 0 или 1 элемента 0 инверсий
    if n <= 1:
        return arr, 0

    m = n // 2
    L = arr[:m]
    R = arr[m:]

    # Рекурсивный вызов для левой и правой половин
    L, inv_L = merge_sort_and_count(L)
    R, inv_R = merge_sort_and_count(R)

    len_L = len(L)
    len_R = len(R)
    l = r = 0
    i = 0
    sorted_arr = [0] * n
    
    # Суммируем инверсии из левой и правой частей
    inversions = inv_L + inv_R

    # Основной цикл слияния
    while l < len_L and r < len_R:
        # Ставим '<=', так как равные элементы НЕ образуют инверсию
        if L[l] <= R[r]:
            sorted_arr[i] = L[l]
            l += 1
        else:
            # Нашли случай, когда L[l] > R[r]
            sorted_arr[i] = R[r]
            # R[r] меньше всех оставшихся элементов в L (от l до len_L)
            inversions += (len_L - l)
            r += 1
        i += 1

    # Забираем оставшиеся элементы из L
    while l < len_L:
        sorted_arr[i] = L[l]
        l += 1
        i += 1

    # Забираем оставшиеся элементы из R
    while r < len_R:
        sorted_arr[i] = R[r]
        r += 1
        i += 1

    return sorted_arr, inversions


def main():
    # Читаем сразу все данные для максимальной скорости
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    # Считываем n элементов массива
    array = [int(x) for x in input_data[1:n + 1]]

    # Запускаем сортировку с подсчетом инверсий
    _, total_inversions = merge_sort_and_count(array)

    # Выводим только итоговое количество инверсий
    print(total_inversions)


if __name__ == "__main__":
    main()