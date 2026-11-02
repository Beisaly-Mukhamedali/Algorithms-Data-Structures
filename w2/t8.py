class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def main():
    # 1. Считываем данные из стандартного ввода
    n = int(input())
    numbers = list(map(int, input().split()))

    # 2. Строим односвязный список согласно условию задачи
    head = Node(numbers[0])
    curr = head
    for num in numbers[1:]:
        curr.next = Node(num)
        curr = curr.next

    # 3. Алгоритм Кадана для поиска максимальной суммы подмассива
    # max_so_far хранит глобальный максимум
    # max_ending_here хранит максимальную сумму подмассива, заканчивающегося в текущем узле
    max_so_far = head.val
    max_ending_here = head.val

    # Начинаем обход со второго узла
    curr = head.next
    while curr:
        # Решаем: выгодно ли прибавить текущее значение к накопившейся сумме
        # или лучше начать новый отрезок с текущего элемента
        max_ending_here = max(curr.val, max_ending_here + curr.val)
        
        # Обновляем глобальный максимум
        max_so_far = max(max_so_far, max_ending_here)
        
        curr = curr.next

    # 4. Выводим результат
    print(max_so_far)

if __name__ == "__main__":
    main()