def is_diagonally_dominant(matrix):
    n = len(matrix)
    strictly_dominant_count = 0

    for i in range(n):
        row_sum = sum(matrix[i]) - matrix[i][i]  # Sum of non-diagonal elements in row i
        if matrix[i][i] < row_sum:
            return "NO", 0
        if matrix[i][i] > row_sum:
            strictly_dominant_count += 1

    if strictly_dominant_count > 0:
        return "YES", strictly_dominant_count
    else:
        return "NO", 0

# Read input
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Determine if the matrix is diagonally dominant
result, count = is_diagonally_dominant(matrix)

# Print the results
print(result)
if result == "YES":
    print(count)