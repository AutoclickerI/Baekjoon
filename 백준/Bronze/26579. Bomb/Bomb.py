def count_destroyed_enemies(map_grid, r, c, rows, cols):
    count = 0
    # Up
    for i in range(r - 1, -1, -1):
        if map_grid[i][c] == '#':
            break
        if map_grid[i][c] == '@':
            count += 1

    # Down
    for i in range(r + 1, rows):
        if map_grid[i][c] == '#':
            break
        if map_grid[i][c] == '@':
            count += 1

    # Left
    for j in range(c - 1, -1, -1):
        if map_grid[r][j] == '#':
            break
        if map_grid[r][j] == '@':
            count += 1

    # Right
    for j in range(c + 1, cols):
        if map_grid[r][j] == '#':
            break
        if map_grid[r][j] == '@':
            count += 1

    return count

def best_bomb_position(test_cases):
    results = []
    for case in test_cases:
        rows, cols, map_grid = case
        max_enemies = -1
        best_position = (-1, -1)
        
        for r in range(rows):
            for c in range(cols):
                if map_grid[r][c] == '.':
                    enemies_destroyed = count_destroyed_enemies(map_grid, r, c, rows, cols)
                    if enemies_destroyed > max_enemies:
                        max_enemies = enemies_destroyed
                        best_position = (r, c)
        
        results.append(best_position)
    
    return results

# Input parsing
n = int(input())
test_cases = []
for _ in range(n):
    r, c = map(int, input().split())
    map_grid = [input().strip() for _ in range(r)]
    test_cases.append((r, c, map_grid))

# Process and output results
results = best_bomb_position(test_cases)
for position in results:
    print(f"{position[0]}, {position[1]}")