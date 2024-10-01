def calculate_fuel(M, N, alpha, passenger_weights):
    # Общая масса людей
    total_people_mass = sum(passenger_weights)
    
    # Общая масса самолета с людьми
    total_mass = M + total_people_mass
    
    # Вычисляем необходимую массу топлива
    alpha_factor = alpha / 1000.0
    if (1 - alpha_factor) <= 0:
        return "Impossible"
    
    # Выражаем T
    T = total_mass * alpha_factor / (1 - alpha_factor)
    
    return T

# Чтение данных
M, N, alpha = map(int, input().strip().split())
passenger_weights = list(map(int, input().strip().split()))

# Получаем результат
result = calculate_fuel(M, N, alpha, passenger_weights)

# Вывод результата
if result == "Impossible":
    print(result)
else:
    print(f"{result:.10f}")  # выводим с точностью не менее 10 знаков