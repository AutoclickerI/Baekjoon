X, Y, I = map(int, input().split())
field = [[False] * (X + 1) for _ in range(Y + 1)]

for _ in range(I):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            field[y][x] = True

# True 값 카운트
plowed_count = sum(row.count(True) for row in field)
print(plowed_count)
