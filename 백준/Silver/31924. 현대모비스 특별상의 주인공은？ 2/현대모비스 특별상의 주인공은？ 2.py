# 격자판에서 MOBIS의 개수를 세는 함수
def count_mobis(grid):
    N = len(grid)
    target = "MOBIS"
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]
    count = 0

    def in_bounds(x, y):
        return 0 <= x < N and 0 <= y < N

    def find_mobis(x, y):
        nonlocal count
        for dx, dy in directions:
            found = True
            for k in range(5):
                nx, ny = x + k * dx, y + k * dy
                if not in_bounds(nx, ny) or grid[nx][ny] != target[k]:
                    found = False
                    break
            if found:
                count += 1

    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'M':
                find_mobis(i, j)

    return count

# 입력 처리 부분
N = int(input())
grid = [input().strip() for _ in range(N)]

# 결과 출력
print(count_mobis(grid))