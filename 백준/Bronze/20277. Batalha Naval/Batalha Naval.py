def is_valid_placement(N, ships):
    # Initialize a 10x10 grid to track occupied positions
    board = [[False] * 10 for _ in range(10)]
    
    for D, L, R, C in ships:
        R -= 1  # Convert to 0-indexed
        C -= 1  # Convert to 0-indexed
        
        if D == 0:  # Horizontal ship
            if C + L > 10:  # Check if it exceeds the board limits
                return 'N'
            for i in range(L):
                if board[R][C + i]:  # Check for overlap
                    return 'N'
                board[R][C + i] = True
        
        elif D == 1:  # Vertical ship
            if R + L > 10:  # Check if it exceeds the board limits
                return 'N'
            for i in range(L):
                if board[R + i][C]:  # Check for overlap
                    return 'N'
                board[R + i][C] = True
    
    return 'Y'

# Read input
N = int(input())
ships = [tuple(map(int, input().split())) for _ in range(N)]

# Validate the ship placement
result = is_valid_placement(N, ships)
print(result)