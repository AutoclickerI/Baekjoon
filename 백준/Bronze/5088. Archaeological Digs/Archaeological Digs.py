g = lambda: [*map(int, input().split())]

while'1'<(s:=input()):
    X, Y = map(int, s.split())
    board = [[0] * Y for _ in range(X)]
    
    for _ in range(int(input())):x, y = g();board[x][y] += 1
    
    ans = 0
    for _ in range(int(input())):x, y = g();ans += board[x][y]
    print(ans)