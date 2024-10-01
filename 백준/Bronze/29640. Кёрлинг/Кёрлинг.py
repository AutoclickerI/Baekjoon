def squared_distance(x, y):
    # Calculate the squared distance from (x, y) to the origin (0, 0)
    return x * x + y * y

def calculate_score(n, ends_data):
    score_team1 = 0
    score_team2 = 0
    
    for i in range(n):
        m, k = ends_data[i][0]  # m: number of stones for team 1, k: for team 2
        team1_stones = ends_data[i][1]  # Coordinates of team 1 stones
        team2_stones = ends_data[i][2]  # Coordinates of team 2 stones
        
        # Calculate the squared distances of all stones from both teams
        team1_distances = [squared_distance(x, y) for x, y in team1_stones]
        team2_distances = [squared_distance(x, y) for x, y in team2_stones]
        
        # Find the closest stone from each team
        min_team1_distance = min(team1_distances) if team1_distances else float('inf')
        min_team2_distance = min(team2_distances) if team2_distances else float('inf')
        
        if min_team1_distance < min_team2_distance:
            # Team 1 scores points for all their stones that are closer than the closest team 2 stone
            for d in team1_distances:
                if d < min_team2_distance:
                    score_team1 += 1
        elif min_team2_distance < min_team1_distance:
            # Team 2 scores points for all their stones that are closer than the closest team 1 stone
            for d in team2_distances:
                if d < min_team1_distance:
                    score_team2 += 1
    
    return f"{score_team1}:{score_team2}"

def main():
    n = int(input())  # Number of completed ends
    ends_data = []
    
    for _ in range(n):
        m, k = map(int, input().split())  # m: number of stones for team 1, k: number of stones for team 2
        team1_stones = [tuple(map(int, input().split())) for _ in range(m)]
        team2_stones = [tuple(map(int, input().split())) for _ in range(k)]
        ends_data.append(((m, k), team1_stones, team2_stones))
    
    # Calculate and print the score
    result = calculate_score(n, ends_data)
    print(result)

if __name__ == "__main__":
    main()