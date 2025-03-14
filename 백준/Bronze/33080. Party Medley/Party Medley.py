from itertools import combinations

def find_balanced_teams(N, M, ratings):
    # Initialize the count of valid teams and the maximum rating
    valid_teams_count = 0
    max_team_rating = -1
    
    # Iterate over all combinations of three different students
    for i, j, k in combinations(range(N), 3):
        team_ratings = [ratings[i], ratings[j], ratings[k]]
        team_sum = sum(team_ratings)
        rating_difference = max(team_ratings) - min(team_ratings)
        
        # Check if the team is balanced
        if rating_difference <= M:
            valid_teams_count += 1
            max_team_rating = max(max_team_rating, team_sum)
    
    # If no valid team is found, return -1
    if valid_teams_count == 0:
        return -1
    else:
        return valid_teams_count, max_team_rating

# Read input
N, M = map(int, input().split())
ratings = list(map(int, input().split()))

# Get the result
result = find_balanced_teams(N, M, ratings)

# Print the result
if result == -1:
    print(result)
else:
    print(result[0], result[1])
