import sys
input=sys.stdin.readline
from collections import deque

def main():
    n = int(input())  # количество операций
    swords = deque()  # используем deque для эффективных операций
    for _ in range(n):
        command = input().strip()  # читаем команду
        if command.startswith("add"):
            _, x = command.split()
            swords.append(int(x))  # добавляем меч справа
        elif command == "take":
            if swords:
                swords.pop()  # забираем меч справа
        elif command == "mum!":
            if len(swords) > 1:
                # Берем левую половину мечей
                mid = len(swords) // 2
                # Добавляем левую половину справа
                swords.rotate(-mid)

    # Выводим результат
    print(len(swords))  # количество оставшихся мечей
    if swords:
        print(" ".join(map(str, swords)))  # номера мечей слева направо

if __name__ == "__main__":
    main()