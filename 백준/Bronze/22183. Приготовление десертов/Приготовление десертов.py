f=lambda:[*map(int,input().split())]

n,m,k=f()
board = [[[1] * k for _ in range(m)] for _ in range(n)]
for _ in[0]*f()[0]:
    a,b=f()
    board[a-1][b-1] = [0] * k
for _ in[0]*f()[0]:
    a,b=f()
    for i in range(n):
        board[i][a-1][b-1] = 0
for _ in[0]*f()[0]:
    a,b=f()
    for i in range(m):
        board[a-1][i][b-1] = 0
print(sum(sum(j)for i in board for j in i))