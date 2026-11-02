class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def main():
    # Чтение данных
    n, k = map(int, input().split())
    words = input().split()

    # 1. Построение односвязного списка
    head = Node(words[0])
    curr = head
    for word in words[1:]:
        curr.next = Node(word)
        curr = curr.next
    tail = curr  # Запоминаем текущий последний элемент

    # 2. Находим новый хвост (K-й элемент)
    new_tail = head
    for _ in range(k - 1):
        new_tail = new_tail.next

    # Новая голова — это следующий за K-м элементом узел
    new_head = new_tail.next

    # 3. Перенаправляем ссылки для циклического сдвига
    tail.next = head       # Соединяем конец со старым началом
    new_tail.next = None   # Обрываем список после K-го элемента

    # 4. Обходим список от new_head и выводим
    curr = new_head
    result = []
    while curr:
        result.append(curr.val)
        curr = curr.next

    print(*result)

if __name__ == "__main__":
    main()