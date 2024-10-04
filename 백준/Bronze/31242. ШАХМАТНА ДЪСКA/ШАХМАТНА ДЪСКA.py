# Directions for knight moves: (x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1),
# (x + 1, y + 2), (x + 1, y - 2), (x - 1, y + 2), (x - 1, y - 2)
knight_moves = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]

# Function to check if two positions are valid knight moves
def is_valid_knight_move(x1, y1, x2, y2):
    for dx, dy in knight_moves:
        if x1 + dx == x2 and y1 + dy == y2:
            return True
    return False

# Read the board input (4x5 matrix)
board = [list(map(int, input().split())) for _ in range(4)]

# Find positions of numbers 1 to 20 on the board
positions = {}
for i in range(4):
    for j in range(5):
        positions[board[i][j]] = (i, j)

# Start from number 1 and check if each subsequent move is valid
current_number = 1
while current_number < 20:
    x1, y1 = positions[current_number]
    x2, y2 = positions[current_number + 1]
    if not is_valid_knight_move(x1, y1, x2, y2):
        break
    current_number += 1

# Output the last valid number reached
print(current_number)