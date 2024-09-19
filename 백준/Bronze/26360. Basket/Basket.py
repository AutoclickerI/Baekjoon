def calculate_basketball_points(X, initial_success, stopped, additional_throws):
    points = 0
    
    if initial_success:
        points += X
    
    if stopped:
        if initial_success:
            additional_throws_count = 1
        else:
            additional_throws_count = X
        additional_points = sum(int(throw) for throw in additional_throws[:additional_throws_count])
        points += additional_points
    
    return points

# Read input values
X = int(input().strip())
initial_success = int(input().strip())
stopped = int(input().strip())
additional_throws = []

if stopped:
    if initial_success:
        additional_throws.append(input().strip())
    else:
        additional_throws = [input().strip() for _ in range(X)]

# Calculate and print the final score
print(calculate_basketball_points(X, initial_success, stopped, additional_throws))