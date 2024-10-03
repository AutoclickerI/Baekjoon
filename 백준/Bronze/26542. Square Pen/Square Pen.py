def largest_square_area(s, field):
    # Initialize the DP table with all 0s
    dp = [[0] * s for _ in range(s)]
    max_side = 0  # Keep track of the largest square side length found

    for i in range(s):
        for j in range(s):
            if field[i][j] == '.':
                if i == 0 or j == 0:
                    # First row or column, can only have squares of size 1
                    dp[i][j] = 1
                else:
                    # Take the minimum of top, left, and top-left neighbors
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                
                # Update the maximum side length found so far
                max_side = max(max_side, dp[i][j])

    # The area of the largest square is side_length^2
    return max_side * max_side

# Read input
n = int(input())  # Number of test cases
for _ in range(n):
    s = int(input())  # Size of the square field
    field = [input().strip() for _ in range(s)]
    
    # Find and print the area of the largest square pen
    print(largest_square_area(s, field))