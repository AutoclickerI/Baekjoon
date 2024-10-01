def rotate_counterclockwise(grid):
    N = len(grid)
    # Rotate the grid 90 degrees counterclockwise
    return [[grid[j][N - i - 1] for j in range(N)] for i in range(N)]

def is_sorted_grid(grid):
    N = len(grid)
    # Check if the grid is sorted in rows and columns
    for i in range(N):
        for j in range(1, N):
            # Check if each row is sorted
            if grid[i][j] < grid[i][j - 1]:
                return False
            # Check if each column is sorted
            if grid[j][i] < grid[j - 1][i]:
                return False
    return True

def main():
    # Read input
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    # Try rotating the grid up to 3 times counterclockwise
    for rotation in range(4):
        if is_sorted_grid(grid):
            print(rotation)
            return
        # Rotate the grid 90 degrees counterclockwise
        grid = rotate_counterclockwise(grid)

if __name__ == "__main__":
    main()