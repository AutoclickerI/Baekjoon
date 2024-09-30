def min_key_presses(n, text):
    presses = 0
    shift_on = False  # Флаг, указывающий на то, включен ли Shift

    for char in text:
        if char.isupper() or char in "!?$()":
            if not shift_on:  # Если Shift не включен, а его нужно включить
                presses += 1
                shift_on = True
            presses += 1  # Нажатие для самого символа
        else:
            if char!=' ':  # Нужно отключить Shift
                shift_on = False
            presses += 1  # Нажатие для самого символа

    return presses

# Пример использования:
n = int(input())  # Читаем количество символов
text = input()  # Читаем строку
print(min_key_presses(n, text))