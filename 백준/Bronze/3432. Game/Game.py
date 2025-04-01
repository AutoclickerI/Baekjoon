def solve():
    import sys
    input = sys.stdin.readline
    
    Z = int(input().strip())
    results = []
    
    for _ in range(Z):
        board = [input().strip() for _ in range(5)]
        
        a_win = False
        b_win = False
        
        # Function to check if three characters are the same
        def check_three(chars):
            if chars == "AAA":
                return "A"
            if chars == "BBB":
                return "B"
            return None
        
        # Check horizontal rows
        for i in range(5):
            for j in range(3):
                res = check_three(board[i][j:j+3])
                if res == "A":
                    a_win = True
                elif res == "B":
                    b_win = True
        
        # Check vertical columns
        for j in range(5):
            for i in range(3):
                col_segment = board[i][j] + board[i+1][j] + board[i+2][j]
                res = check_three(col_segment)
                if res == "A":
                    a_win = True
                elif res == "B":
                    b_win = True
        
        # Check main diagonal (top-left to bottom-right)
        for i in range(3):
            for j in range(3):
                diag_segment = board[i][j] + board[i+1][j+1] + board[i+2][j+2]
                res = check_three(diag_segment)
                if res == "A":
                    a_win = True
                elif res == "B":
                    b_win = True
        
        # Check anti-diagonals (top-right to bottom-left)
        for i in range(3):
            for j in range(2, 5):
                anti_diag_segment = board[i][j] + board[i+1][j-1] + board[i+2][j-2]
                res = check_three(anti_diag_segment)
                if res == "A":
                    a_win = True
                elif res == "B":
                    b_win = True
        
        # Decide outcome
        if a_win and not b_win:
            results.append("A wins")
        elif b_win and not a_win:
            results.append("B wins")
        else:
            results.append("draw")
    
    print("\n".join(results))


if __name__ == '__main__':
    solve()
