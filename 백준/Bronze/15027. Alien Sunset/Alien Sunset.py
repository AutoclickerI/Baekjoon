def solve():
    import sys
    input = sys.stdin.readline

    N = int(input().strip())
    settlements = []
    H_max = 0
    for _ in range(N):
        parts = input().split()
        H = int(parts[0])
        R = int(parts[1])
        T = int(parts[2])
        H_max = max(H_max, H)
        dark = [False] * H
        # Для каждого часа от 0 до H-1 определяем, светло или темно.
        # Согласно условию, в рассвет (R) и закат (T) всегда темно.
        # Остальное – смотрим по порядку:
        if R < T:
            # Светло, если строго между R и T.
            for x in range(H):
                if x == R or x == T:
                    dark[x] = True
                else:
                    # если x строго между R и T, то светло, иначе темно.
                    if R < x < T:
                        dark[x] = False
                    else:
                        dark[x] = True
        else:
            # Если R > T, то светло, если x строго между R и T по циклу.
            # То есть, если x после R (x > R) или x до T (x < T) – это светло.
            for x in range(H):
                if x == R or x == T:
                    dark[x] = True
                else:
                    # Если x попадает в интервал (R, H-1] или [0, T), то светло.
                    if (x > R or x < T):
                        dark[x] = False
                    else:
                        dark[x] = True
        settlements.append((H, dark))
    
    # Лимит в часах – 1825 дней по самой длинной планете
    limit = 1825 * H_max

    # Перебираем время от 0 до limit-1
    for t in range(limit):
        all_dark = True
        for H, dark in settlements:
            if not dark[t % H]:
                all_dark = False
                break
        if all_dark:
            sys.stdout.write(str(t))
            return
    sys.stdout.write("impossible")


if __name__ == '__main__':
    solve()
