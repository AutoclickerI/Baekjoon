N=int(input())
board=[[*map(int,input().replace(*'.0').replace(*'X1'))]for _ in[0]*N]
cnt=0
def S(r,y,x):
    global cnt
    assert cnt<N*N
    cnt+=1
    assert 0<=r<=4
    print(f'S {r} {y} {x}')
    if r%2:
        assert 0<=x-2<x+2<N and 0<=y-1<y+1<N
        S=[[1,0,1,1,1],
           [1,0,1,0,1],
           [1,1,1,0,1]]
        for ypos in range(3):
            for xpos in range(5):
                board[y-1+ypos][x-2+xpos]^=S[ypos][xpos]
    else:
        assert 0<=x-1<x+1<N and 0<=y-2<y+2<N
        S=[[1,1,1],
           [1,0,0],
           [1,1,1],
           [0,0,1],
           [1,1,1]]
        for ypos in range(5):
            for xpos in range(3):
                board[y-2+ypos][x-1+xpos]^=S[ypos][xpos]

def C(r,y,x):
    global cnt
    assert cnt<N*N
    cnt+=1
    assert 0<=r<=4
    print(f'C {r} {y} {x}')
    if r==0:
        assert 0<=x-1<x+1<N and 0<=y-2<y+2<N
        C=[[1,1,1],
           [1,0,0],
           [1,0,0],
           [1,0,0],
           [1,1,1]]
        for ypos in range(5):
            for xpos in range(3):
                board[y-2+ypos][x-1+xpos]^=C[ypos][xpos]
    if r==1:
        assert 0<=x-2<x+2<N and 0<=y-1<y+1<N
        C=[[1,1,1,1,1],
           [1,0,0,0,1],
           [1,0,0,0,1]]
        for ypos in range(3):
            for xpos in range(5):
                board[y-1+ypos][x-2+xpos]^=C[ypos][xpos]
    if r==2:
        assert 0<=x-1<x+1<N and 0<=y-2<y+2<N
        C=[[1,1,1],
           [0,0,1],
           [0,0,1],
           [0,0,1],
           [1,1,1]]
        for ypos in range(5):
            for xpos in range(3):
                board[y-2+ypos][x-1+xpos]^=C[ypos][xpos]
    if r==3:
        assert 0<=x-2<x+2<N and 0<=y-1<y+1<N
        C=[[1,0,0,0,1],
           [1,0,0,0,1],
           [1,1,1,1,1]]
        for ypos in range(3):
            for xpos in range(5):
                board[y-1+ypos][x-2+xpos]^=C[ypos][xpos]

def Ldot(r,y,x):
    # 5*3 pattern for L' shape
    
    # r=0
    # ...
    # ...
    # .BX
    # X.X
    # ...
    
    # r=1
    # .X...
    # ..B..
    # .XX..
    
    # r=2
    # ...
    # X.X
    # XB.
    # ...
    # ...
    
    # r=3
    # ..XX.
    # ..B..
    # ...X.
    S(r,y,x)
    C(r,y,x)

def Z(r,y,x):
    # 6*3 pattern for Z shape
    
    # r=0
    # ...
    # ...
    # XB.
    # .XX
    # ...
    # ...
    
    # r=1
    # ...X..
    # ..BX..
    # ..X...
    
    # r=2
    # ...
    # ...
    # XX.
    # .BX
    # ...
    # ...
    
    # r=3
    # ...X..
    # ..XB..
    # ..X...
    
    if r==0:
        Ldot(r,y,x)
        Ldot(r^2,y+1,x)
    if r==1:
        Ldot(r,y,x+1)
        Ldot(r^2,y,x)
    if r==2:
        Ldot(r,y,x)
        Ldot(r^2,y-1,x)
    if r==3:
        Ldot(r,y,x-1)
        Ldot(r^2,y,x)

def L(r,y,x):
    # 5*5 pattern for L shape
    
    # r=0
    # .....
    # .....
    # ..b..
    # .XXX.
    # ...X.
    
    # r=1
    # .....
    # .X...
    # .Xb..
    # XX...
    # .....
    
    # r=2
    # .X...
    # .XXX.
    # ..b..
    # .....
    # .....
    
    # r=3
    # .....
    # ...XX
    # ..bX.
    # ...X.
    # .....
    if r==0:
        S(r,y,x)
        C(r,y,x)
        S(3+r&3,y+1,x)
        C(3+r&3,y+1,x)
    if r==1:
        S(r,y,x)
        C(r,y,x)
        S(3+r&3,y,x-1)
        C(3+r&3,y,x-1)
    if r==2:
        S(r,y,x)
        C(r,y,x)
        S(3+r&3,y-1,x)
        C(3+r&3,y-1,x)
    if r==3:
        S(r,y,x)
        C(r,y,x)
        S(3+r&3,y,x+1)
        C(3+r&3,y,x+1)

def I(r,y,x):
    # 6*5 pattern for I shape

    # r=0
    # .....
    # .....
    # ..b..
    # .X...
    # .X...
    # .....

    # r=1
    # ......
    # .XX...
    # ...b..
    # ......
    # ......
    
    # r=2
    # .....
    # ...X.
    # ...X.
    # ..b..
    # .....
    # .....

    # r=3
    # ......
    # ......
    # ..b...
    # ...XX.
    # ......
    if r==0:
        Ldot(r,y+1,x)
        L(r,y,x)
    if r==1:
        Ldot(r,y,x-1)
        L(r,y,x)
    if r==2:
        Ldot(r,y-1,x)
        L(r,y,x)
    if r==3:
        Ldot(r,y,x+1)
        L(r,y,x)

def dot(r,y,x):
    # 8*7 pattern for . shape

    # r=0
    # .......
    # .......
    # ....X..
    # ...B...
    # .......
    # .......
    # .......
    # .......
    
    # r=1
    # ........
    # ........
    # ........
    # ....B...
    # .....X..
    # ........
    # ........
    
    # r=2
    # .......
    # .......
    # .......
    # .......
    # ...B...
    # ..X....
    # .......
    # .......
    
    # r=3
    # ........
    # ........
    # ..X.....
    # ...B....
    # ........
    # ........
    # ........
    if r==0:
        C(r,y+1,x)
        I(r+3&3,y+2,x-1)
        I(r,y+1,x)
        I(r,y-1,x)
        I(r+1&3,y,x+1)
    if r==1:
        C(r,y,x-1)
        I(r+3&3,y-1,x-2)
        I(r,y,x-1)
        I(r,y,x+1)
        I(r+1&3,y+1,x)
    if r==2:
        C(r,y-1,x)
        I(r+3&3,y-2,x+1)
        I(r,y-1,x)
        I(r,y+1,x)
        I(r+1&3,y,x-1)
    if r==3:
        C(r,y,x+1)
        I(r+3&3,y+1,x+2)
        I(r,y,x-1)
        I(r,y,x+1)
        I(r+1&3,y-1,x)

marker_prev=N//2-2
marker_next=N//2

# upper left
for posy in range(marker_prev):
    for posx in range(marker_prev):
        if board[posy][posx]==1:
            if board[posy][posx+1]==1:
                C(1,posy+1,posx+2)
            else:
                S(1,posy+1,posx+2)

# lower left
for posy in range(marker_next,N)[::-1]:
    for posx in range(marker_prev):
        if board[posy][posx]==1:
            if board[posy][posx+1]==1:
                S(1,posy-1,posx+2)
            else:
                C(1,posy-1,posx+2)

# lower right
for posy in range(marker_next,N)[::-1]:
    for posx in range(marker_next,N)[::-1]:
        if board[posy][posx]==1:
            if board[posy-1][posx]==1:
                S(0,posy-2,posx-1)
            else:
                C(0,posy-2,posx-1)

# upper right
for posy in range(marker_prev):
    for posx in range(marker_next+2,N)[::-1]:
        if board[posy][posx]==1:
            if board[posy][posx-1]==1:
                S(1,posy+1,posx-2)
            else:
                C(1,posy+1,posx-2)

# right 2 fill
for posx in range(marker_next,marker_next+2)[::-1]:
    for posy in range(marker_prev-2):
        if board[posy][posx]==1:
            if board[posy+1][posx]==1:
                C(2,posy+2,posx-1)
            else:
                S(0,posy+2,posx-1)

# right upper corner
for posx in range(marker_next,marker_next+2)[::-1]:
    state=board[marker_prev-2][posx],board[marker_prev-1][posx]
    if state==(1,1):
        Ldot(0,marker_prev-2,posx-1)
    if state==(0,1):
        Z(0,marker_prev-2,posx-1)
    if state==(1,0):
        Ldot(2,marker_prev-1,posx-1)

# left 2 fill
for posx in range(marker_prev):
    state=board[marker_prev][posx],board[marker_prev+1][posx]
    if state==(1,1):
        Ldot(2,marker_prev+1,posx+1)
    if state==(0,1):
        Ldot(0,marker_prev,posx+1)
    if state==(1,0):
        Z(0,marker_prev,posx+1)

# bottom 2 fill
for posy in range(marker_next,N)[::-1]:
    state=board[posy][marker_prev],board[posy][marker_prev+1]
    if state==(1,1):
        Ldot(1,posy-1,marker_prev+1)
    if state==(0,1):
        Ldot(3,posy-1,marker_prev)
    if state==(1,0):
        Z(1,posy-1,marker_prev)

# right 2 fill
for posx in range(marker_next,N)[::-1]:
    state=board[marker_prev][posx],board[marker_prev+1][posx]
    if state==(1,1):
        Ldot(0,marker_prev,posx-1)
    if state==(0,1):
        Z(0,marker_prev,posx-1)
    if state==(1,0):
        Ldot(2,marker_prev+1,posx-1)

# top 2 fill
for posy in range(marker_prev):
    state=board[posy][marker_prev],board[posy][marker_prev+1]
    if state==(1,1):
        Ldot(3,posy+1,marker_prev)
    if state==(0,1):
        Z(1,posy+1,marker_prev)
    if state==(1,0):
        Ldot(1,posy+1,marker_prev+1)

state=board[marker_prev][marker_prev],board[marker_prev][marker_prev+1]
if state==(1,1):
    I(3,marker_prev-1,marker_prev-1)
if state==(0,1):
    I(2,marker_prev+2,marker_prev)
if state==(1,0):
    I(2,marker_prev+2,marker_prev-1)

state=board[marker_prev+1][marker_prev],board[marker_prev+1][marker_prev+1]
if state==(1,1):
    I(3,marker_prev,marker_prev-1)
if state==(0,1):
    dot(1,marker_prev,marker_prev)
if state==(1,0):
    dot(1,marker_prev,marker_prev-1)
    
assert sum(map(sum,board))==0