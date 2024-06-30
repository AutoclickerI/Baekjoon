def calculate_positions(n, team_vasya, team_opponent, standings):
    def get_position(standings, team_name):
        standings.sort(key=lambda x: (-x[1], x[0]))  # сортировка по очкам и по названию команды
        for i, (name, points) in enumerate(standings):
            if name == team_name:
                return i + 1
        return -1

    # Копируем текущую турнирную таблицу для каждого сценария
    standings_win = standings[:]
    standings_draw = standings[:]
    standings_loss = standings[:]

    # Находим текущие очки команд Васи и соперника
    points_vasya = 0
    points_opponent = 0
    for i, (name, points) in enumerate(standings):
        if name == team_vasya:
            points_vasya = points
            standings_win[i] = (name, points + 3)
            standings_draw[i] = (name, points + 1)
        elif name == team_opponent:
            points_opponent = points
            standings_draw[i] = (name, points + 1)

    # Обновляем таблицы с учетом возможных исходов матча
    for i, (name, points) in enumerate(standings):
        if name == team_opponent:
            standings_win[i] = (name, points)
            standings_draw[i] = (name, points + 1)
            standings_loss[i] = (name, points + 3)

    # Получаем позиции команды Васи для каждого сценария
    pos_win = get_position(standings_win, team_vasya)
    pos_draw = get_position(standings_draw, team_vasya)
    pos_loss = get_position(standings_loss, team_vasya)

    return pos_win, pos_draw, pos_loss


# Ввод данных
n = int(input().strip())
team_vasya = input().strip()
team_opponent = input().strip()

standings = []
for _ in range(n):
    data = input().strip().split()
    team_name = data[0]
    team_points = int(data[1])
    standings.append((team_name, team_points))

# Расчет позиций
pos_win, pos_draw, pos_loss = calculate_positions(n, team_vasya, team_opponent, standings)

# Вывод результата
print(pos_win, pos_draw, pos_loss)
