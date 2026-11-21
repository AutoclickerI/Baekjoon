def main():
    import sys

    s = sys.stdin.read()
    if not s:
        return
    s = s.rstrip('\n')
    
    # Для каждого символа, если он буква, мы можем изменить её регистр.
    # Будем рассматривать два варианта: первая буква оставлена заглавной или строчной.
    # Для каждого варианта вычисляем суммарное число изменений.
    cost_upper = 0
    cost_lower = 0
    
    # Для последующей реконструкции результата, сохраняем флаги нужного регистра для буквы.
    # Например, True означает, что букву нужно сделать заглавной.
    pattern_upper = []  # для варианта, когда первая буква должна быть заглавной
    pattern_lower = []  # для варианта, когда первая буква должна быть строчной
    
    letter_index = 0  # номер буквы в строке (игнорируя не буквы)
    for ch in s:
        if ch.isalpha():
            # В варианте pattern_upper: буква на четной позиции (0,2,...) должна быть заглавной,
            # на нечетной – строчной.
            desired_upper = (letter_index % 2 == 0)
            pattern_upper.append(desired_upper)
            # Вариант pattern_lower: первая буква строчная, потом чередование.
            desired_lower = (letter_index % 2 == 1)
            pattern_lower.append(desired_lower)
            
            # Считаем стоимость изменения для обоих вариантов.
            # Если ch уже в нужном регистре, то изменение не требуется.
            if desired_upper:
                if not ch.isupper():
                    cost_upper += 1
            else:
                if not ch.islower():
                    cost_upper += 1
                    
            if desired_lower:
                if not ch.isupper():
                    cost_lower += 1
            else:
                if not ch.islower():
                    cost_lower += 1
            
            letter_index += 1
        # Если символ не буква, то он не влияет на стоимость и остаётся неизменным.
    
    # Выбираем вариант с меньшей суммарной стоимостью.
    use_upper = (cost_upper <= cost_lower)
    
    result_chars = []
    letter_index = 0
    for ch in s:
        if ch.isalpha():
            if use_upper:
                # Если в выбранном варианте для этой буквы true, то делаем заглавную, иначе – строчную.
                if pattern_upper[letter_index]:
                    result_chars.append(ch.upper())
                else:
                    result_chars.append(ch.lower())
            else:
                if pattern_lower[letter_index]:
                    result_chars.append(ch.upper())
                else:
                    result_chars.append(ch.lower())
            letter_index += 1
        else:
            result_chars.append(ch)
    
    sys.stdout.write("".join(result_chars))
    

if __name__ == '__main__':
    main()