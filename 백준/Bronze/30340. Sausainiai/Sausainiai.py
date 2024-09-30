import sys
input=sys.stdin.readline
def optimal_cookie_difference(N, cookies):
    # Sort cookies based on the sum (a_i + b_i) in descending order
    cookies.sort(key=lambda x: x[0] + x[1], reverse=True)
    
    A = 0  # Antanas' total score
    B = 0  # Bronius' total score
    
    # Simulate the game
    for i in range(N):
        if i % 2 == 0:
            # Antanas' turn (even index)
            A += cookies[i][0]
        else:
            # Bronius' turn (odd index)
            B += cookies[i][1]
    
    # Return the difference A - B
    return A - B

# Input reading and function call
N = int(input())
cookies = [tuple(map(int, input().split())) for _ in range(N)]
print(optimal_cookie_difference(N, cookies))