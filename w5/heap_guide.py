import heapq

# --- 1. Heapify: Преобразование списка в кучу за O(N) ---
a = [2, 5, 0, 1, 10, 8, -4, 3, 12, 9]
heapq.heapify(a)  # Модифицирует список на месте за O(N)
print("Куча (Min-Heap):", a)

# --- 2. Heap Push: Вставка элемента (O(log N)) ---
heapq.heappush(a, 4)  # Добавляет элемент и восстанавливает структуру
print("После heappush(4):", a)

# --- 3. Heap Pop: Извлечение минимального элемента (O(log N)) ---
min_val = heapq.heappop(a)  # Извлекает и возвращает корень кучи
print("Извлеченный минимум:", min_val)  # -4
print("Куча после heappop:", a)

# --- 4. Heap Peak: Просмотр минимального элемента за O(1) ---
min_peak = a[0]  # Минимальный элемент всегда находится на индексе 0
print("Минимум без извлечения:", min_peak)

# --- 5. Heap Sort: Пирамидальная сортировка за O(N log N) ---
def heap_sort(arr):
    heapq.heapify(arr)  # Превращаем в кучу за O(N)
    new_list = [0] * len(arr)
    for i in range(len(arr)):
        new_list[i] = heapq.heappop(arr)  # Поочередно достаем минимальный элемент
    return new_list

arr_to_sort = [5, -2, 10, 0, 1, 8, 3]
print("Отсортированный массив:", heap_sort(arr_to_sort))

# --- 6. Эмуляция Max-Heap (Куча максимума) ---
# В Python heapq работает только как Min-Heap, поэтому числа инвертируют (* -1)
b = [2, 5, 10, 12, 9]
b_neg = [-x for x in b]  # Инвертируем знаки
heapq.heapify(b_neg)

# Вставка числа 7 в Max-Heap:
heapq.heappush(b_neg, -7)  # Передаем -7

# Извлечение максимума:
max_val = -heapq.heappop(b_neg)  # Возвращаем исходный знак
print("Извлеченный максимум:", max_val)

# --- 7. Очередь с приоритетами для кортежей (Priority Queue) ---
# При отправке кортежей (tuple) сортировка идет по первому элементу
priority_queue = []
heapq.heappush(priority_queue, (1, "Task A"))  # (Приоритет, Данные)
heapq.heappush(priority_queue, (3, "Task C"))
heapq.heappush(priority_queue, (2, "Task B"))

priority, task = heapq.heappop(priority_queue)
print(f"Первая задача: {task} с приоритетом {priority}")  # Task A