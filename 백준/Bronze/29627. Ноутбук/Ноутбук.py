def time_to_minutes(hh_mm):
    """Convert time in hh:mm format to minutes since 00:00."""
    hh, mm = map(int, hh_mm.split(":"))
    return hh * 60 + mm

def calculate_battery_percentage(n, x, y, switch_times):
    # Начальные значения
    current_time = 0  # время в минутах (начало дня 00:00 = 0 минут)
    battery = 100.0  # стартовый заряд батареи
    charging = True  # ноутбук заряжается от сети

    # Обрабатываем каждую смену питания
    for switch_time in switch_times:
        next_time = time_to_minutes(switch_time)
        elapsed_time = next_time - current_time
        
        # Изменение заряда в зависимости от текущего источника питания
        if charging:
            battery += elapsed_time * (100 / y)  # зарядка
        else:
            battery -= elapsed_time * (100 / x)  # разрядка
        
        # Ограничиваем заряд от 0 до 100
        battery = min(max(battery, 0.0), 100.0)
        
        # Обновляем текущее время и переключаем источник питания
        current_time = next_time
        charging = not charging

    # Обрабатываем время до 23:59 (1440 минут с начала дня)
    elapsed_time = 1439 - current_time
    if charging:
        battery += elapsed_time * (100 / y)
    else:
        battery -= elapsed_time * (100 / x)

    # Ограничиваем заряд от 0 до 100
    battery = min(max(battery, 0.0), 100.0)
    
    # Возвращаем заряд с точностью до трех знаков
    return round(battery, 3)

# Чтение входных данных
n, x, y = map(int, input().split())
switch_times = [input().strip() for _ in range(n)]

# Расчет и вывод результата
result = calculate_battery_percentage(n, x, y, switch_times)
print(result)