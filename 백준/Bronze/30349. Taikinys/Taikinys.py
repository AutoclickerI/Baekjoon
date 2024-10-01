def main():
    # Reading inputs
    M, N = map(int, input().split())  # Window dimensions (width, height)
    A, B = map(int, input().split())  # Target dimensions (width, height)
    X, Y = map(int, input().split())  # Wind displacement (horizontal, vertical)
    
    min_penalty = float('inf')  # Initialize minimum penalty as infinite
    hit = False  # Flag to check if a hit is possible

    # Iterate over all possible starting points in the window
    for Xp in range(M):
        for Yp in range(N):
            # Calculate the final position after displacement
            target_x = Xp + X
            target_y = Yp + Y
            
            # Check if the final position hits the target
            if 0 <= target_x < A and 0 <= target_y < B:
                hit = True
                # Calculate penalty
                penalty = target_x + target_y
                # Track the minimum penalty
                min_penalty = min(min_penalty, penalty)
    
    # Output the result
    if hit:
        print(min_penalty)
    else:
        print("NEPATAIKYS")

if __name__ == "__main__":
    main()