import sys

def main():
    # Читаем все входные данные сразу для высокой скорости
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    a = []
    
    while True:
        try:
            cmd = int(next(it))
        except StopIteration:
            break
            
        if cmd == 0:
            # Выход из программы
            break
            
        elif cmd == 1:
            # 1 x p: вставка элемента x на позицию p
            x = int(next(it))
            p = int(next(it))
            a.insert(p, x)
            
        elif cmd == 2:
            # 2 p: удаление элемента с позиции p
            p = int(next(it))
            a.pop(p)
            
        elif cmd == 3:
            # 3: печать всего списка (или -1, если пуст)
            if not a:
                print(-1)
            else:
                print(*(a))
                
        elif cmd == 4:
            # 4 p1 p2: переместить элемент из p1 на позицию p2
            p1 = int(next(it))
            p2 = int(next(it))
            val = a.pop(p1)
            a.insert(p2, val)
            
        elif cmd == 5:
            # 5: развернуть весь список
            a.reverse()
            
        elif cmd == 6:
            # 6 x: циклический сдвиг влево на x элементов
            x = int(next(it))
            if a:
                x %= len(a)
                a = a[x:] + a[:x]
                
        elif cmd == 7:
            # 7 x: циклический сдвиг вправо на x элементов
            x = int(next(it))
            if a:
                x %= len(a)
                a = a[-x:] + a[:-x] if x > 0 else a

if __name__ == '__main__':
    main()