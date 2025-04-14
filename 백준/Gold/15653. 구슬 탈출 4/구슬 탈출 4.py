N,M=map(int,input().split())

b=tuple((*input(),)for _ in[0]*N)

v={0,b}

from collections import deque

dq=deque([(b,'')])

def move(board,d):
    board=[[*i]for i in board]
    dy,dx=[(-1,0),(1,0),(0,1),(0,-1)]['UDRL'.find(d)]
    success=fail=0
    for i in range(1,N-1):
        for j in range(1,M-1):
            if board[i][j]=='R':
                yr,xr=i,j
            if board[i][j]=='B':
                yb,xb=i,j
    while board[yr+dy][xr+dx]=='.':
        board[yr][xr]='.'
        yr+=dy
        xr+=dx
        board[yr][xr]='R'
    if board[yr+dy][xr+dx]=='O':
        board[yr][xr]='.'
        success=1
    while board[yb+dy][xb+dx]=='.':
        board[yb][xb]='.'
        yb+=dy
        xb+=dx
        board[yb][xb]='B'
    if board[yb+dy][xb+dx]=='O':
        fail=1
    while board[yr+dy][xr+dx]=='.':
        board[yr][xr]='.'
        yr+=dy
        xr+=dx
        board[yr][xr]='R'
    if board[yr+dy][xr+dx]=='O':
        board[yr][xr]='.'
        success=1
    if fail:
        return 0
    if success:
        return 1
    return tuple((*i,)for i in board)

while dq:
    b,s=dq.popleft()
    for d in'UDLR':
        t=move(b,d)
        if t==1:
            print(len(s)+1)
            exit()
        elif t not in v:
            v.add(t)
            dq+=(t,s+d),
            
print(-1)