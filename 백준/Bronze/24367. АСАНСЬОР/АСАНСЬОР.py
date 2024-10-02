from itertools import combinations

# Ввод данных
M, N = map(int, input().split())
weights = list(map(int, input().split()))

# Сортируем веса, чтобы легче было перебирать группы
weights.sort(reverse=True)

# Переменная для хранения минимального количества поездок
trips = 0

# Пока есть дети, которых нужно перевезти
while weights:
    trips += 1
    current_weight = 0
    current_passengers = 0
    to_remove = []
    
    # Проходим по весам детей, начиная с самого тяжелого
    for i, w in enumerate(weights):
        if current_passengers < M and current_weight + w <= N:
            current_weight += w
            current_passengers += 1
            to_remove.append(i)
    
    # Удаляем тех, кто уже был перевезен в этой поездке
    for i in reversed(to_remove):
        weights.pop(i)

# Выводим минимальное количество поездок
print(trips)