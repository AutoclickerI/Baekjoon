board=[list(map(int,input().split()))for _ in range(9)]
def getyx(n):
    return n//9,n%9

def check(y,x):
    for i in range(9):
        if i!=x and board[y][i]==board[y][x]:
            return False
        if i!=y and board[i][x]==board[y][x]:
            return False
    for i in range(3):
        for j in range(3):
            if (y//3*3+i,x//3*3+j)!=(y,x) and board[y//3*3+i][x//3*3+j]==board[y][x]:
                return False
    return True
def backtracking(n):
    y,x=getyx(n)
    while n<81 and board[y][x]:
        n+=1
        y,x=getyx(n)
        
    if n==81:
        for line in board:
            print(*line)
        raise
    for i in range(1,10):
        tmp=board[y][x]
        board[y][x]=i
        if check(y,x):
            backtracking(n+1)
        board[y][x]=tmp

try:
    backtracking(0)
except:
    pass