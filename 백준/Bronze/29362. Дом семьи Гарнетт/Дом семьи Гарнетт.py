def main():

    import sys

    input_data = sys.stdin.read().strip().split()

    if not input_data:

        return

    it = iter(input_data)

    n = int(next(it))

    m = int(next(it))

    

    wells = []

    # Читаем матрицу, находим координаты скважин.

    for i in range(n):

        for j in range(m):

            if int(next(it)) == 1:

                wells.append((i, j))

    # Убедимся, что скважин ровно две.

    if len(wells) != 2:

        return

    (rA, cA), (rB, cB) = wells[0], wells[1]

    

    best_area = 0

    

    # Сценарий 1: хотим, чтобы A была внутри, а B – снаружи.

    # Внутри означает: для well A: T <= rA and rA+1 <= B, L <= cA and cA+1 <= R.

    # Снаружи для well B: хотя бы одно из условий не выполняется.

    # Рассмотрим варианты, где мы обрезаем участок с одной стороны.

    

    # Обрезка сверху: вырезаем верхнюю часть, чтобы исключить B.

    # Выбираем T = rB + 1, B = n, L = 0, R = m.

    # Чтобы A была внутри, необходимо: rA >= T  (т.е. rA >= rB + 1).

    if rA >= rB + 1:

        area = (n - (rB + 1)) * m

        best_area = max(best_area, area)

    

    # Обрезка снизу: B исключается, если B = rB, T = 0, L = 0, R = m.

    # Для A: rA+1 <= rB  (т.е. rA <= rB - 1).

    if rA + 1 <= rB:

        area = rB * m

        best_area = max(best_area, area)

    

    # Обрезка слева: устанавливаем L = cB + 1, R = m, T = 0, B = n.

    # Для A: cA >= cB + 1.

    if cA >= cB + 1:

        area = n * (m - (cB + 1))

        best_area = max(best_area, area)

    

    # Обрезка справа: устанавливаем R = cB, L = 0, T = 0, B = n.

    # Для A: cA + 1 <= cB.

    if cA + 1 <= cB:

        area = n * cB

        best_area = max(best_area, area)

    

    # Сценарий 2: хотим, чтобы B была внутри, а A – снаружи.

    # Аналогично:

    

    # Обрезка сверху: T = rA + 1, B = n, L = 0, R = m.

    # Для B: rB >= rA + 1.

    if rB >= rA + 1:

        area = (n - (rA + 1)) * m

        best_area = max(best_area, area)

    

    # Обрезка снизу: B = rA, T = 0, L = 0, R = m.

    # Для B: rB + 1 <= rA.

    if rB + 1 <= rA:

        area = rA * m

        best_area = max(best_area, area)

    

    # Обрезка слева: L = cA + 1, R = m, T = 0, B = n.

    # Для B: cB >= cA + 1.

    if cB >= cA + 1:

        area = n * (m - (cA + 1))

        best_area = max(best_area, area)

    

    # Обрезка справа: R = cA, L = 0, T = 0, B = n.

    # Для B: cB + 1 <= cA.

    if cB + 1 <= cA:

        area = n * cA

        best_area = max(best_area, area)

    

    print(best_area)

if __name__ == '__main__':

    main()