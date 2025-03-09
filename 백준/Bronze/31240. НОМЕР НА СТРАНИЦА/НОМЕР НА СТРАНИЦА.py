def main():
    import sys
    s = sys.stdin.read().strip()
    if not s:
        return
    n = len(s)
    
    # Если первая цифра равна '0', то число i имеет ведущий ноль – недопустимо.
    if s[0] == '0':
        sys.stdout.write("0")
        return

    count = 0
    # Перебираем возможное разбиение: i = s[:pos], n = s[pos:]
    # pos от 1 до n-1, чтобы обе части были непустыми.
    for pos in range(1, n):
        # Если первая цифра второй части равна '0', разбиение недопустимо.
        if s[pos] == '0':
            continue
        
        len_i = pos
        len_n = n - pos
        # Если длина i меньше длины n, то i однозначно меньше n.
        if len_i < len_n:
            count += 1
        # Если длины равны – сравниваем лексикографически.
        elif len_i == len_n:
            if s[:pos] <= s[pos:]:
                count += 1
        # Если len_i > len_n, то i больше n – недопустимо.
    sys.stdout.write(str(count))
    
if __name__ == '__main__':
    main()
